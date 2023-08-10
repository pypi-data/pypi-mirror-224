import datetime
import os

from src.DwxClient import DwxClient


class TickProcessor(object):
    def __init__(self, db,
                 sleep_delay=0.005,  # 5 ms for time.sleep()
                 max_retry_command_seconds=10,  # retry to send to commend for 10 seconds if not successful.
                 verbose=True
                 ):
        self.dat = {}
        self.lot = 0.01
        self.price = 0.0
        self.bid = 0.0
        self.ask = 0.0
        self.time_frame = 'H1'
        self.prices = {}
        self.symbol = "AUDUSD"
        self.db = db

        # if true, it will randomly try to open and close orders every few seconds.

        self.account_data = {}
        self._MarketStates = {}

        self.live_data: dict = {}
        self.MT4_directory_path = os.getenv("AppData") + "\\MetaQuotes\\Terminal" \
                                                         "\\3212703ED955F10C7534BE8497B221F4\\MQL4\\Files\\"
        self.server_status = {
            "status": "online",
            "server_time": datetime.datetime.utcnow().timestamp(),
            "server_time_utc": datetime.datetime.utcnow().isoformat(),
            "server_time_local": datetime.datetime.utcnow().astimezone().isoformat(),
            "message": "Connected to MetaTrader"
        }

        self.last_open_time = datetime.datetime.utcnow()
        self.last_modification_time = datetime.datetime.utcnow()

        self.dwx = DwxClient(self, metatrader_dir_path=self.MT4_directory_path, sleep_delay=sleep_delay,
                             max_retry_command_seconds=max_retry_command_seconds, verbose=verbose,db=self.db)

        # request historic data:
        self.end = datetime.datetime.utcnow()
        self.start = self.end - datetime.timedelta(days=30)  # last 30 days

        self.on_historic_trades()

        self.on_order_event()

    def on_historic_trades(self):
        print(f'historic_trades: {len(self.dwx.historic_trades)}')
        self.server_status['message'] = "On historic trades  " + str(datetime.datetime.utcnow()) + " trades " + str(
            len(self.dwx.historic_trades))
        self.account_data['trades'] = self.dwx.historic_trades

    def on_message(self, message):

        if message['type'] == 'ERROR':
            print(message['type'], '|', message['error_type'], '|', message['description'])
            self.server_status['status'] = 'offline'
            self.server_status['message'] = message['description']

        elif message['type'] == 'INFO':
            print(message['type'], '|', message['message'])
            self.server_status['message'] = message['message']

        elif message['type'] == 'TICK':
            print(message['type'], '|', message['symbol'], '|', message['bid'], '|', message['ask'])
            self.server_status['message'] = message['symbol']

        elif message['type'] == 'BAR':
            print(message['type'], '|', message['symbol'], '|', message['time_frame'], '|', message['time'], '|',
                  message['open'], '|', message['high'], '|', message['low'], '|', message['close'], '|',
                  message['volume'])
            self.server_status['message'] = message['symbol']

    # triggers when an order is added or removed, not when only modified.
    def on_order_event(self):

        print(f'on_order_event. open_orders: {len(self.dwx.open_orders)} open orders')
        self.server_status['message'] = "order event  " + str(datetime.datetime.utcnow()) + " open orders " + \
                                        str(len(self.dwx.open_orders))+"        \n"+self.dwx.historic_trades.__str__()

    ##########################################################################
    # Here were i write my trading strange

    def save_to_db(self, _db):
        _db.save(self.dat)

##############################################################################
