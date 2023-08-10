from datetime import datetime

import requests
import pandas as pd
import tablib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from ta.trend import MACD

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

    _df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                      'quote_asset_volume', 'num_trades', 'taker_buy_base', 'taker_buy_quote',
                                      'ignore'])
    _df['timestamp'] = pd.to_datetime(_df['timestamp'], unit='ms')
    return _df


def calculate_macd(df_):
    series = pd.Series(df_['close'], index=df_['timestamp'], name='close', dtype='float', fastpath=False)
    close_prices = series
    macd_ = MACD(close_prices)
    signal_ = macd_.macd_signal()
    return macd_, signal_


def simulate_trading(macd_, signal_):
    balance_ = 1000  # Initial balance in USDT
    close_signal_=0
    order_id = 1  # Initial order id

    close_time = 0  # Initial close time
    start_balance = balance_  # Initial start balance
    close_balance = 0  # Initial close balance
    close_price = 0  # Initial close price
    status = 'open'  # Initial status
    order_type = 'limit'  # Initial order type
    side = 'BUY'  # Initial side
    price = 1.34  # Initial price
    volume = 1000  # Initial volume

    open_time = [datetime.now()]
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
    }]

    if signal_ > 0:
        side = 'BUY'
        price = price + 0.01
        volume = volume + 1000
        start_balance = start_balance + price * volume
        status = 'open'
        order_id = order_id + 1
        open_time.append(datetime.now())
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
            'side': side})

    elif signal_ < 0:
        side = 'SELL'
        price = price + 0.01
        volume = volume + 1000
        start_balance = start_balance + price * volume
        status = 'open'
        order_id = order_id + 1
        open_time.append(datetime.now())
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
            'side': side})

    if close_signal_ > 0:
        side = 'BUY'
        price = price + 0.01
        volume = volume + 1000
        start_balance = start_balance + price * volume
        status = 'close'
        order_id = order_id + 1
        close_time= datetime.now()
        positions.append({
            'open_time': open_time,
            'close_time': close_time,
            'order_id': order_id,
            'price': price,
            'volume': volume,
            'start_balance': start_balance,
            'order_type': order_type,
            'close_price': close_price,
            'close_balance': close_balance
        })

    if close_signal_ < 0:
        side = 'BUY'
        price = price + 0.01
        volume = volume + 1000
        start_balance = start_balance + price * volume
        status = 'close'
        order_id = order_id + 1
        close_time= datetime.now()
        positions.append({
            'open_time': open_time,
            'close_time': close_time,
            'order_id': order_id,
            'price': price,
            'volume': volume,
            'start_balance': start_balance,
            'order_type': order_type,
            'close_price': close_price,
            'close_balance': close_balance
        })

    for i in positions:
        if status == 'open':
            count = i.get('open_time').count(datetime.now())

            print("Total Open orders " + str(count))
    return balance_


def display_chart(
        df_):
    root = tk.Tk()
    root.title('Cryptocurrency Chart')

    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(df_['timestamp'], df_['close'], label='Close Price')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    root.mainloop()


if __name__ == '__main__':
    df = fetch_candlestick_data('BTCUSDT', '1m', 1000)
    macd, signal = calculate_macd(df)
    balance = simulate_trading(macd, signal)
    print(balance)
    display_chart(df)
