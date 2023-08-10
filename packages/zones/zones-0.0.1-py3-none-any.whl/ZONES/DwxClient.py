import datetime
import json
import os
from os.path import join, exists
from threading import Thread, Lock
from time import sleep
from traceback import print_exc
import joblib
import numpy as np
import pandas as pd
import requests
import self

from pandas import DataFrame

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm._libsvm import predict
from ta.trend import MACD
from tensorflow_estimator.python.estimator.canned.timeseries import model

"""Client class
This class includes all of the functions needed for communication with MT4/MT5. 

"""


def try_read_file(file_path: str) -> object:
    try:
        if exists(file_path):
            with open(file_path) as f:
                text = f.read()
            return text
    # can happen if mql writes to the file. don't print anything here.
    except (IOError, PermissionError):
        pass
    except Exception as e:
        print(e)
        print_exc()
    return ''


def preprocess_data(data):
    # Calculate technical indicators (example: moving averages)
    data['SMA_10'] = data['close'].rolling(window=10).mean()
    data['SMA_50'] = data['close'].rolling(window=50).mean()

    # Create target variable (future price) by shifting the Close price
    data['Target'] = data['close'].shift(-1)

    # Drop rows with NaN values in the Target column (last row will have NaN)
    data.dropna(subset=['Target'], inplace=True)

    # Create features for the model
    x = data[['SMA_10', 'SMA_50']]
    y = data['Target']

    return x, y


def try_remove_file(file_path):
    for _ in range(10):
        try:
            os.remove(file_path)
            break
        except (IOError, PermissionError):
            pass
        except Exception as e:
            print(e)
            print_exc()


def mm_size(sl_: float = 0.005):
    risk_percentage = 10
    max_lot = 100000
    min_lot = 0.01

    lots = risk_percentage * 1.0 / 100 / sl_ / 1000000
    if lots > max_lot:
        lots = max_lot
    elif lots < min_lot:
        lots = min_lot
    return lots


def get_signal(prediction_):
    return 1 if prediction_ > 0 else -1


def calculate_macd(data=None):
    series = pd.Series(data)
    print(series)
    close_prices = series

    if len(close_prices) < 2:
        return 0, 0
    macd, signal = MACD(close_prices)
    return macd, signal


def predict_signal(symbol, data):
    if data is None or len(data) < 2:
        print("Not enough data for prediction")
        return 0
    macd, signal = calculate_macd(data)
    prediction = predict(np.array([macd, signal]).reshape(1, -1))
    print('Prediction: ', prediction)
    return get_signal(prediction_=prediction.array[0][0])


class DwxClient(object):
    def __init__(self, event_handler=None, metatrader_dir_path: str = "",
                 sleep_delay=0.005,  # 5 ms for time.sleep()
                 # retry to send to commend for 10 seconds if not successful.
                 max_retry_command_seconds=10,
                 # to load orders from file on initialization.
                 load_orders_from_file=True,
                 verbose=True, db=None
                 ):
        self.db_schema = None

        self.stop_loss = None
        self.take_profit = None
        self.path_account_data = None
        self._last_account_data_str = None
        self.balance = None
        self.sl = None
        self.model = None
        self.db = db
        self.clf_model = None
        self._last_market_data = {}
        self.mql_dir_path = metatrader_dir_path
        self.clf_save = None

        self.bar_data1 = None
        self.df_ = None
        self.market_data = {}
        self.data = {}
        self.dat = {}
        self.live_data = {}
        self.ask: float = 0.0
        self.bid: float = 0.0
        self.price: float = 0.0
        self.time_frame = 'H1'
        self.prices = {}
        self.symbol = 'AUDUSD'
        self.account_data = {}
        self.server_status = {
            "status": "off",
            "message": "not connected",
            "server_time": datetime.datetime.now()

        }
        self.last_open_time = datetime.datetime.now()
        self.last_modification_time = 0
        self.check_historic_trades = {}
        self.event_handler = event_handler
        self.sleep_delay = sleep_delay
        self.max_retry_command_seconds = max_retry_command_seconds
        self.load_orders_from_file = load_orders_from_file
        self.verbose = verbose
        self.command_id = 0
        self.num_command_files = 50
        self._last_messages_millis = 0
        self._last_open_orders_str = ""
        self._last_messages_str = ""
        self._last_market_data_str = ""
        self._last_bar_data_str = ""
        self._last_historic_data_str = ""
        self._last_historic_trades_str = ""
        self.open_orders = {}
        self.account_info = {}
        self.bar_data = {}
        self.historic_data = {}
        self.historic_trades = {}
        self.last_bar_data = {}

        if not exists(metatrader_dir_path):
            # create directory
            os.makedirs(metatrader_dir_path)
            print('ERROR: metatrader_dir_path does not exist!')
        self.path_orders = join(metatrader_dir_path + "\\Files\\",
                                "DWX\\", 'DWX_Orders.txt')
        self.path_messages = join(metatrader_dir_path,
                                  "DWX\\", 'DWX_Messages.txt')
        self.path_market_data = join(metatrader_dir_path,
                                     "DWX\\", 'DWX_Market_Data.txt')
        self.path_bar_data: str = join(metatrader_dir_path,
                                       "DWX\\", 'DWX_Bar_Data.txt')
        self.path_historic_data = join(metatrader_dir_path,
                                       "DWX\\", 'DWX_Historic_Data.txt')
        self.path_historic_trades = join(metatrader_dir_path,
                                         'DWX\\', 'DWX_Historic_Trades.txt')
        self.path_orders_stored = join(metatrader_dir_path,
                                       'DWX\\', 'DWX_Orders_Stored.txt')
        self.path_messages_stored = join(metatrader_dir_path,
                                         'DWX\\', 'DWX_Messages_Stored.txt')
        self.path_commands_prefix = join(metatrader_dir_path,
                                         'DWX\\', 'DWX_Commands_')
        self.path_commands_account_data = join(metatrader_dir_path,
                                               'DWX\\', 'DWX_Commands_Account_Data.txt')
        self.ACTIVE = True
        self.START = False
        self.lock = Lock()
        self.load_messages()
        if self.load_orders_from_file:
            self.load_orders()
        self.reset_command_ids()
        # no need to wait.
        if self.event_handler:
            self.check_historic_data_Thread = Thread(target=self.check_historic_data, args=())
            self.check_historic_data_Thread.daemon = True
            self.check_historic_data_Thread.start()

            self.check_market_data_Thread = Thread(target=self.check_market_data, args=())
            self.check_market_data_Thread.daemon = True
            self.check_market_data_Thread.start()

            self.check_bar_data_Thread = Thread(target=self.check_bar_data, args=())
            self.check_bar_data_Thread.daemon = True
            self.check_bar_data_Thread.start()

            self.check_account_data_Thread = Thread(target=self.check_account_data, args=())

            self.messages_thread = Thread(target=self.check_messages, args=())
            self.messages_thread.daemon = True
            self.messages_thread.start()

            self.open_orders_thread = Thread(target=self.check_open_orders, args=())
            self.open_orders_thread.daemon = True
            self.open_orders_thread.start()

        self.start_()
        self._t = Thread(target=self.trader_, args=())
        self._t.daemon = True
        self._t.start()

    """START can be used to check if the client has been initialized.  
    """

    def start_(self):
        self.START = True
        self.server_status['status'] = "running"

    """Tries to read a file. 
    """

    def set_trade_symbols(self, symbols=None, time_frame=None):

        if time_frame is None:
            time_frame = ['H1', 'M30']
        if symbols is None:
            symbols = ['EURUSD']
        self.server_status['message'] = "subscribed to " + str(symbols.__str__()) + "   " + str(
            datetime.datetime.utcnow())

        # subscribe to tick data:
        if self.subscribe_symbols(symbols):
            # subscribe to bar data:
            for symbol in symbols:
                self.subscribe_symbols_bar_data([[symbol, time_frame]])

    """Tries to remove a file.
    """

    """Regularly checks the file for open orders and triggers
    the event_handler.on_order_event() function.
    """

    def close_signal(self, symbol, data):
        return get_signal(prediction_=predict_signal(symbol=symbol, data=data))

    def check_open_orders(self):

        while self.ACTIVE:

            self.server_status['message'] = " check_open_orders " + str(datetime.datetime.utcnow())
            sleep(self.sleep_delay)
            if self.START:
                text = try_read_file(self.path_orders)
                if len(text.strip()) == 0 or text == self._last_open_orders_str:
                    continue
                self._last_open_orders_str = text
                data = json.loads(str(text))

                self.server_status['message'] = " open_orders " + str(data)
                new_event = False
                for order_id, order in self.open_orders.items():
                    # also triggers if a pending order got filled?
                    if order_id not in data['orders'].keys():
                        new_event = True
                        if self.verbose:
                            print('Order removed: ', order)
                for order_id, order in data['orders'].items():
                    if order_id not in self.open_orders:
                        new_event = True
                        if self.verbose:
                            print('New order: ', order)

                self.account_info = data['account_info']
                self.balance = data['balance']
                self.open_orders = data['orders']
                with open(self.path_orders_stored, 'w') as f:
                    f.write(json.dumps(data))
                if self.event_handler is not None and new_event:
                    self.event_handler.on_order_event()
            else:
                if self.event_handler is not None:
                    self.event_handler.on_order_event()

    """Regularly checks the file for messages and triggers
    the event_handler.on_message() function.
    """

    def check_messages(self):

        while self.ACTIVE:
            sleep(self.sleep_delay)

            self.server_status['message'] = " check_messages " + str(datetime.datetime.utcnow())
            if not self.START:
                continue
            text = try_read_file(self.path_messages)
            if len(text.strip()) == 0 or text == self._last_messages_str:
                continue

            self._last_messages_str = text
            data = json.loads(str(text))
            self.server_status['message'] = " messages " + str(data)

            # use sorted() to make sure that we don't miss messages
            # because of (int(millis) > self._last_messages_millis).
            for millis, message in sorted(data.items()):
                if int(millis) > self._last_messages_millis:
                    self._last_messages_millis = int(millis)
                    print(message)
                    if self.event_handler is not None:
                        self.event_handler.on_message(message)

            with open(self.path_messages_stored, 'w') as f:
                f.write(json.dumps(data))
                f.close()

    """Regularly checks the file for market data and triggers
    the event_handler.on_tick() function.
    """

    def signal(self, symbol: str = 'AUDUSD', data: dict = None):
        self.server_status['message'] = 'signal ' + symbol + "   "
        print(str(self.market_data))

        if data.values() is None: return
        data2 = pd.DataFrame(data=data, columns=['open', 'high', 'low', 'close', 'volume'])

        series = pd.Series(data=data2['close'].values, dtype='float64', index=data2.index)

        macd0 = MACD(series)

        print("signal " + str(macd0.macd_signal()))
        self.server_status['message'] = "signal " + symbol + "   " + str(macd0.macd_signal())

        if datetime.datetime.utcnow() - self.last_open_time > datetime.timedelta(minutes=10):
            macd = 1
        else:
            macd = -1
        if macd > 0:
            return 1
        elif macd < 0:
            return -1
        else:
            return 0

    def trader_(self):

        self.last_open_time = datetime.datetime.utcnow()
        # SET TRADING symbols
        symbols = ['EURUSD', 'NZDUSD']
        time_frames = ['H1']

        if self.set_trade_symbols(symbols=symbols, time_frame=time_frames):
            self.subscribe_symbols_bar_data(
                [[symbol, time_frame] for symbol in symbols for time_frame in time_frames])

            self.subscribe_symbols_bar_data([[self.symbol, self.time_frame],
                                             [self.symbol, self.time_frame]])
            self.server_status['status'] = "== Live Trading =="
            self.server_status['message'] = "trader initialized " + str(datetime.datetime.utcnow())
        else:
            self.server_status['status'] = "== Live Trading =="
            self.server_status['message'] = "trader failed to initialize " + str(datetime.datetime.utcnow())
            return
        while self.ACTIVE:
            # Create a 2D array to store the data
            if self.bar_data1 is None:
                print("last_bar_data is None" + str(self.bar_data1))

                self.server_status['message'] = "last_bar_data is None " + str(datetime.datetime.utcnow())
                return
            self.dat = self.bar_data1
            print('dat ' + str(self.dat))
            print(self.dat)
            row = ['open', 'high', 'low', 'close', 'volume']
            self.df_ = DataFrame(data=self.dat, columns=row)
            self.df_['open'] = self.dat['open']
            self.df_['high'] = self.dat['high']
            self.df_['low'] = self.dat['low']
            self.df_['close'] = self.dat['close']
            self.df_['volume'] = self.dat['volume']

            #  Saving the data to database

            self.df_.to_sql("candles", con=self.db, schema=self.db_schema, if_exists='append', index=False)
            self.server_status['status'] = '======== Live Trading ======='
            self.server_status['message'] = "trader started \n" + str(
                datetime.datetime.utcnow()) + self.df_.__str__()
            ma = self._last_market_data
            self.ask = ma[self.symbol]['ask']
            self.bid = ma[self.symbol]['bid']
            print("ask " + str(self.ask))
            print("bid " + str(self.bid))
            self.server_status['message'] = self.symbol + " BID " + str(self.bid) + " ASK " + str(self.ask) + "\n" \
                                            + self.df_.__str__()
            # Learning rate
            # Replace X_new with your new data for trading decision

            columns = ['open', 'high', 'low', 'close', 'volume']
            labels = columns
            self.server_status['message'] = self.symbol + " BID " + str(self.bid) + " ASK " + str(self.ask)
            features = self.df_[columns].values
            x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.09)
            clf = MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100))
            clf = clf.fit(x_train, y_train)
            print("clf " + clf.__str__())

            accuracy = clf.score(x_train, y_train)

            print(' training data accuracy ', accuracy * 100)
            accuracy = clf.score(x_test, y_test)
            print(' testing data accuracy ', accuracy * 100)
            ypredict = clf.predict(x_train)
            print('\n Training classification report\n', classification_report(y_train, ypredict))
            ypredict = clf.predict(y_train)

            print("predicted " + str(ypredict))
            print('\n Testing classification report\n', classification_report(y_test, ypredict))
            self.server_status['status'] = 'Learning rate' + str(
                clf.score(x_train, y_train)) + '%' + '\n' + self.df_.__str__()
            # Output a pickle file for the model
            joblib.dump(clf, 'src/saved_model.pkl')
            self.server_status['message'] = self.symbol + " BID " + str(self.bid) + " ASK " + str(self.ask)
            self.on_tick(
                symbol=self.symbol,
                bid=self.bid,
                ask=self.ask)

    ####################################################################

    def on_tick(self, symbol='EURUSD', bid=0.0, ask=0.0):

        account_balance = self.get_account_data()

        print("account_balance " + str(account_balance))

        self.server_status['message'] = str(datetime.datetime.utcnow()) + "\n symbol " + str(symbol) + "\n bid " + str(
            bid) + "\n ask " + str(ask)
        self.server_status['server_time'] = datetime.datetime.now()

        self.live_trading(symbol=self.symbol, bid=bid, ask=ask,
                          close_signal_=self.close_signal(symbol=self.symbol, data=self.dat),
                          signal_=self.signal(symbol=self.symbol, data=self.dat))

    def get_account_data(self):
        return self.account_data

    def on_historic_data(self, symbol_, time_frame: str, data):
        # you can also access the historic data via self.dwx.historic_data.
        print('historic_data:', symbol_, time_frame, f'{len(data)} bars')
        self.server_status['message'] = "On historic data  " + str(datetime.datetime.utcnow()) + " TimeFrame " + str(
            time_frame) + " bars " + str(len(data))
        self.historic_data['symbol'] = symbol_
        self.historic_data['time_frame'] = time_frame
        self.historic_data['bars'] = data
        self.historic_data['time'] = datetime.datetime.utcnow()
        print("bars " + str(self.historic_data))

        return self.historic_data

    def check_account_data(self) -> dict:

        while self.ACTIVE:
            sleep(self.sleep_delay)
            if self.START:
                text = try_read_file(self.path_account_data)
                if len(text.strip()) == 0 or text == self._last_account_data_str:
                    continue

                self._last_account_data_str = text
                data = json.loads(str(text))
                self.account_data = data
                print(self.account_data)
                if self.event_handler is not None:
                    self.event_handler.on_account_data(symbol=self.account_data['symbol'], data=self.account_data)
                return self.account_data

    def check_market_data(self) -> dict:

        while self.ACTIVE:
            sleep(self.sleep_delay)
            if not self.START:
                continue
            text = try_read_file(self.path_market_data)
            if len(text.strip()) == 0 or text == self._last_market_data_str:
                continue

            self._last_market_data_str = text
            data = json.loads(str(text))
            self.market_data = data
            print(self.market_data)

            if self.event_handler is not None:
                for symbol in data.keys():
                    if symbol not in self._last_market_data or \
                            self.market_data[symbol] != self._last_market_data[symbol]:
                        self._last_market_data[symbol] = self.market_data[symbol]

                        self._last_market_data = data
                        self.on_tick(symbol=symbol,
                                     bid=self._last_market_data[symbol]['bid'],
                                     ask=self._last_market_data[symbol]['ask']
                                     )

            # self.event_handler.market_data(symbol=symbol, data=data[symbol])

        return self.market_data

    """Regularly checks the file for bar data and triggers
    the event_handler.on_bar_data() function.
    """

    def check_bar_data(self) -> None:
        open_ = []
        high_ = []
        low_ = []
        close_ = []
        volume_ = []
        symbol_ = []
        tf_ = []
        time_ = []

        while self.ACTIVE:
            sleep(self.sleep_delay)
            if self.START:
                text = try_read_file(file_path=str(self.path_bar_data))
                if len(text.strip()) == 0 or text == self._last_bar_data_str:
                    continue
                self._last_bar_data_str = text
                data = json.loads(text.__str__())
                self.bar_data = data
                if self.event_handler is None:
                    print("no event handler")

                else:
                    for st in data.keys():
                        if st not in self.last_bar_data or self.bar_data[st] != self.last_bar_data[st]:
                            time_frame = st.split('_')
                            open_ = self.bar_data[st]['open']
                            high_ = self.bar_data[st]['high']
                            low_ = self.bar_data[st]['low']
                            close_ = self.bar_data[st]['close']
                            volume_ = self.bar_data[st]['tick_volume']
                            symbol_ = st
                            tf_ = time_frame
                            time_ = self.bar_data[st]['time']
                            self.last_bar_data[st] = self.bar_data[st]
                            self.last_bar_data = {
                                'open': open_,
                                'high': high_,
                                'low': low_,
                                'close': close_,
                                'volume': volume_,
                                'time': time_,
                                'time_frame': tf_,
                                'symbol': symbol_
                            }
                print("loading bar data..." + str(self.last_bar_data))
                data1: dict = {
                    'open': open_,
                    'high': high_,
                    'low': low_,
                    'close': close_,
                    'volume': volume_,
                    'time': time_,
                    'time_frame': tf_,
                    'symbol': symbol_
                }

                self.bar_data1 = data1

    """Regularly checks the file for historic data and trades and triggers
    the event_handler.on_historic_data() function.
    """

    def check_historic_data(self):

        while self.ACTIVE:

            sleep(self.sleep_delay)
            if not self.START:
                continue
            text = try_read_file(file_path=self.path_historic_data)

            if len(text.strip()) > 0 and text != self._last_historic_data_str:
                self._last_historic_data_str = text
                data = json.loads(text.__str__())
                for st in data.keys():
                    self.historic_data[st] = data[st]
                    if self.event_handler is not None:
                        symbol, time_frame = st.split('_')
                        self.on_historic_data(
                            symbol, time_frame, data[st])
                try_remove_file(self.path_historic_data)

            # also check historic trades in the same thread.
            text = try_read_file(file_path=self.path_historic_trades)

            if len(text.strip()) > 0 and text != self._last_historic_trades_str:
                self._last_historic_trades_str = text

                data = json.loads(text.__str__())

                self.historic_trades = data
                self.event_handler.on_historic_trades()

                try_remove_file(self.path_historic_trades)

    """Loads stored orders from file (in case of a restart). 
    """

    def load_orders(self):
        text = try_read_file(file_path=self.path_orders_stored)
        if len(text.__str__()) > 0:
            self._last_open_orders_str = text
            data = json.loads(text.__str__())
            self.account_info = data['account_info']
            self.open_orders = data['orders']

    """Loads stored messages from file (in case of a restart). 
    """

    def load_messages(self):
        text = try_read_file(self.path_messages_stored)
        if len(text.__str__()) > 0:
            self._last_messages_str = text
            data = json.loads(text.__str__())
            # here we don't have to sort because we just need the latest millis value.
            for millis in data.keys():
                if int(millis) > self._last_messages_millis:
                    self._last_messages_millis = int(millis)

    """Sends a SUBSCRIBE_SYMBOLS command to subscribe to market (tick) data.

    Args:
        symbols (list[str]): List of symbols to subscribe to.
    
    Returns: 
        None

        The data will be stored in self.market_data. 
        On receiving the data the event_handler.on_tick() 
        function will be triggered. 
    
    """

    def subscribe_symbols(self, symbols):
        self.send_command('SUBSCRIBE_SYMBOLS', ','.join(symbols))

        for symbol in symbols:
            if symbol not in self.market_data:
                self.market_data[symbol] = {

                }
                return False

            self.market_data[symbol]['bid'] = 0
            self.market_data[symbol]['ask'] = 0
            return True

    """Sends a SUBSCRIBE_SYMBOLS_BAR_DATA command to subscribe to bar data.

    Kwargs:
        symbols (list[list[str]]): List of lists containing symbol/time frame 
        combinations to subscribe to. For example:
        symbols = [['EURUSD', 'M1'], ['GBPUSD', 'H1']]
    
    Returns:
        None

        The data will be stored in self.bar_data. 
        On receiving the data the event_handler.on_bar_data() 
        function will be triggered. 
    
    """

    def subscribe_symbols_bar_data(self, symbols=None):

        if symbols is None:
            symbols = [['EURUSD', 'H1']]
        data = [f'{st[0]},{st[1]}' for st in symbols]
        self.send_command('SUBSCRIBE_SYMBOLS_BAR_DATA',
                          ','.join(str(p) for p in data))

    """Sends a GET_HISTORIC_DATA command to request historic data. 
    
    Kwargs:
        symbol (str): Symbol to get historic data.
        time_frame (str): Time frame for the requested data.
        start (int): Start timestamp (seconds since epoch) of the requested data.
        end (int): End timestamp of the requested data.
    
    Returns:
        None

        The data will be stored in self.historic_data. 
        On receiving the data the event_handler.on_historic_data()
        function will be triggered. 
    """

    def get_historic_data(self,
                          symbol='EURUSD',
                          time_frame='H1',
                          start=datetime.datetime.utcnow() - datetime.timedelta(days=30),

                          end=datetime.datetime.now()):

        self.data = [symbol, time_frame, start, end]
        self.send_command('GET_HISTORIC_DATA', ','.join(str(p) for p in self.data))

    """Sends a GET_HISTORIC_TRADES command to request historic trades.
    
    Kwargs:
        lookback_days (int): Days to look back into the trade history. The history must also be visible in MT4. 
    
    Returns:
        None

        The data will be stored in self.historic_trades. 
        On receiving the data the event_handler.on_historic_trades() 
        function will be triggered. 
    """

    def get_historic_trades(self,
                            lookback_days=60):
        self.send_command('GET_HISTORIC_TRADES', str(lookback_days))

    """Sends an OPEN_ORDER command to open an order.

    Kwargs:
        symbol (str): Symbol for which an order should be opened. 
        order_type (str): Order type. Can be one of:
            'buy', 'sell', 'buylimit', 'selllimit', 'buystop', 'sellstop'
        lots (float): Volume in lots
        price (float): Price of the (pending) order. Can be zero 
            for market orders. 
        stop_loss (float): SL as absolute price. Can be zero 
            if the order should not have an SL. 
        take_profit (float): TP as absolute price. Can be zero 
            if the order should not have a TP.  
        magic (int): Magic number
        comment (str): Order comment
        expiration (int): Expiration time given as timestamp in seconds. 
            Can be zero if the order should not have an expiration time.  
    
    """

    def open_order(self, symbol='AUDUSD',
                   order_type='buy',
                   lots: float = 0.02,
                   price: float = 0.0,
                   stop_loss: float = 100.5,
                   take_profit: float = 100.4,
                   magic=1,
                   comment='Zones EA',
                   expiration=0):

        data = [symbol, order_type, lots, price, stop_loss,
                take_profit, magic, comment, expiration]
        self.send_command('OPEN_ORDER', ','.join(str(p) for p in data))

    """Sends a MODIFY_ORDER command to modify an order.
    Args:
        ticket (int): Ticket of the order that should be modified.
    Kwargs:
        lots (float): Volume in lots
        price (float): Price of the (pending) order. Non-zero only 
            works for pending orders. 
        stop_loss (float): New stop loss price.
        take_profit (float): New take profit price. 
        expiration (int): New expiration time given as timestamp in seconds. 
            Can be zero if the order should not have an expiration time. 
    """

    def modify_order(self, ticket,
                     lots: float = 0.01,
                     price: float = 1.6,
                     stop_loss: float = 100.9,
                     take_profit: float = 100.3,
                     expiration=0):
        data = [ticket, lots, price, stop_loss, take_profit, expiration]
        self.send_command('MODIFY_ORDER', ','.join(str(p) for p in data))

    """Sends a CLOSE_ORDER command to close an order.
    Args:
        ticket (int): Ticket of the order that should be closed.
    Kwargs:
        lots (float): Volume in lots. If lots=0 it will try to 
            close the complete position. 
    """

    def close_order(self, ticket, lots):
        data = [ticket, lots]
        self.send_command('CLOSE_ORDER', ','.join(str(p) for p in data))

    """Sends a CLOSE_ALL_ORDERS command to close all orders.
    """

    def close_all_orders(self):
        self.send_command('CLOSE_ALL_ORDERS', '')

    """Sends a CLOSE_ORDERS_BY_SYMBOL command to close all orders
    with a given symbol.

    Args:
        symbol (str): Symbol for which all orders should be closed. 
    
    """

    def close_orders_by_symbol(self, symbol):
        self.send_command('CLOSE_ORDERS_BY_SYMBOL', symbol)

    """Sends a CLOSE_ORDERS_BY_MAGIC command to close all orders
    with a given magic number.

    Args:
        magic (str): Magic number for which all orders should 
            be closed. 
    
    """

    def close_orders_by_magic(self, magic):
        self.send_command('CLOSE_ORDERS_BY_MAGIC', magic)

    """Sends a RESET_COMMAND_IDS command to reset stored command IDs. 
    This should be used when restarting the python side without restarting 
    the mql side.

    """

    def reset_command_ids(self):
        self.command_id = 0
        self.send_command("RESET_COMMAND_IDS", "")
        # sleep to make sure it is read before other commands.
        sleep(0.5)

    """Sends a command to the mql server by writing it to 
    one of the command files. 

    Multiple command files are used to allow for fast execution 
    of multiple commands in the correct chronological order. 
    
    """

    def send_command(self, command, content):
        # Acquire lock so that different threads do not use the same
        # command_id or write at the same time.
        self.lock.acquire()
        self.command_id = (self.command_id + 1) % 100000
        end_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.max_retry_command_seconds)
        now = datetime.datetime.utcnow()
        # trying again for X seconds in case all files exist or are
        # currently read from mql side.
        while now < end_time:
            # using 10 different files to increase the execution speed
            # for multiple commands.
            success = False
            for i in range(self.num_command_files):
                # only send commend if the file does not exist so that we
                # do not overwrite all commands.
                file_path = f'{self.path_commands_prefix}{i}.txt'
                if not exists(file_path):
                    try:
                        with open(file_path, 'w') as f:
                            f.write(f'<:{self.command_id}|{command}|{content}:>')
                            f.close()
                        success = True
                        break
                    except Exception as e:
                        print(e)
                        print_exc()
            if success:
                break
            sleep(self.sleep_delay)
            now = datetime.datetime.utcnow()
            print(f'Waiting for {self.max_retry_command_seconds} seconds...')
        # release lock again
        self.lock.release()

    def live_trading(self, symbol='EURUSD', bid: float = 0.0, ask: float = 0.0, close_signal_=0, signal_=0):

        global positions, sl, tp
        self.stop_loss = 0.002
        self.take_profit = 0.003
        now = datetime.datetime.utcnow()
        close_time = 0  # Initial close time
        start_balance = 1000  # self.account_data['balance']
        close_balance = 0  # Initial close balance
        close_price = 0  # Initial close price
        status = 'open'  # Initial status

        order_type = 'buystop'

        open_time = [datetime.datetime.now()]

        if signal_ > 0:
            side = 'BUY'
            price = ask
            sl = float(price - self.stop_loss * price)
            tp = float(price + self.take_profit * price)

            volume = mm_size(sl)

            status = 'open'
            order_id = 0
            order_id = order_id + 1
            open_time.append(datetime.datetime.now())

            positions = [{
                'open_time': open_time,
                'close_time': close_time,
                'order_id': order_id,
                'price': price,
                'volume': volume,
                'start_balance': start_balance,
                'order_type': order_type,
                'close_price': close_price,
                'close_balance': close_balance,
                'status': status,
                'side': side
            }, {
                'open_time': open_time,
                'close_time': close_time,
                'order_id': order_id,
                'price': price,
                'volume': volume,
                'start_balance': start_balance,
                'order_type': order_type,
                'close_price': close_price,
                'close_balance': close_balance,

                'status': status,
                'side': side}]

            self.open_order(symbol=symbol,
                            order_type=order_type,
                            price=price,
                            lots=volume,
                            stop_loss=sl,
                            take_profit=tp)
        elif signal_ < 0:
            price = bid
            side = 'SELL'

            status = 'open'
            order_id = 1

            order_type = 'sellstop'

            sl = float(price + self.stop_loss * price)
            tp = float(price - self.take_profit * price)
            volume = mm_size(sl)

            open_time.append(datetime.datetime.now())
            positions = [{
                'open_time': open_time,
                'close_time': close_time,
                'order_id': order_id,
                'price': price,
                'volume': volume,
                'start_balance': start_balance,
                'order_type': order_type,
                'close_price': close_price,
                'close_balance': close_balance,
                'status': status,
                'side': side
            }, {
                'open_time': open_time,
                'close_time': close_time,
                'order_id': order_id,
                'price': price,
                'volume': volume,
                'start_balance': start_balance,
                'order_type': order_type,
                'close_price': close_price,
                'close_balance': close_balance,
                'status': status,
                'side': side}]
            self.open_order(symbol=symbol,
                            order_type=order_type,
                            price=price,
                            lots=volume,
                            stop_loss=sl,
                            take_profit=tp)

            # Close orders
            if close_signal_ > 0:
                side = 'BUY'

            status = 'close'
            order_id = order_id + 1
            close_time = datetime.datetime.now()
            positions.append({
                'open_time': open_time,
                'close_time': close_time,
                'order_id': order_id,
                'price': price,
                'volume': volume,
                'start_balance': start_balance,
                'order_type': order_type,
                'close_price': close_price,
                'close_balance': close_balance,
                'status': status,
                'side': side
            })
            for ticket in self.open_orders.keys():
                self.close_order(ticket, lots=mm_size(sl))

            if close_signal_ < 0:
                side = 'BUY'

                start_balance = start_balance + price * volume
                status = 'close'
                order_id = order_id + 1
                close_time = datetime.datetime.now()
                positions.append({
                    'open_time': open_time,
                    'close_time': close_time,
                    'order_id': order_id,
                    'price': price,
                    'volume': volume,
                    'start_balance': start_balance,
                    'order_type': order_type,
                    'close_price': close_price,
                    'close_balance': close_balance,
                    'status': status,
                    'side': side
                })
                print(positions.__str__())
                self.server_status['message'] = "On tick " + positions.__str__() + " symbol " + symbol

                for ticket in self.open_orders.keys():
                    self.close_order(ticket, lots=mm_size(tp))
            self.last_modification_time = now
        if now > self.last_modification_time + datetime.timedelta(seconds=10):
            self.last_modification_time = now
            for ticket in self.open_orders.keys():
                self.server_status['message'] = "On tick  " + str(datetime.datetime.utcnow()) + " symbol " + str(symbol)
                self.server_status['server_time'] = datetime.datetime.utcnow()

                self.modify_order(ticket, lots=mm_size(sl), stop_loss=sl, take_profit=tp, expiration=0)

            for i in positions:
                if status == 'open':
                    count = i.get('open_time').count(datetime.datetime.now())

                    print("Total Open orders " + str(count))


api_key = 'YOUR_BINANCE_API_KEY'
api_secret = 'YOUR_BINANCE_API_SECRET'
base_url = 'https://api.binance.us/api/v3'


def fetch_candlestick_data(symbol, interval, limit):
    endpoint = f'{base_url}/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(endpoint, params=params)
    data = response.json()

    df_ = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                      'quote_asset_volume', 'num_trades', 'taker_buy_base', 'taker_buy_quote',
                                      'ignore'])
    df_['timestamp'] = pd.to_datetime(df_['timestamp'], unit='ms')
    return df_
