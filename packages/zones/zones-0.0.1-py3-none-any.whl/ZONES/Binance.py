import pandas as pd
import numpy as np
from binance.client import Client
from matplotlib import pyplot as plt

# Binance API credentials (Replace with your own)
API_KEY = 'odkr6pfbgl10ZM7i2D4kZ8FgOZLDjzs3iAY2IV2E67Cm316dkQs397bScVzhH4b1'
API_SECRET = '3ilQvixaFv3Y1sdZ48jO0JqShoQUU6SdQkbviOAgIB2zHR9xu8J7hQSPZGqzxoTd'
# Initialize Binance US client
client = Client(API_KEY, API_SECRET, tld='us')
print(client.get_open_orders())
print(client.get_account())
client.get_klines(symbol='ETHUSDT',interval='1m', limit=1000)


def get_historical_data(symbol, interval, _limit):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=_limit)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                       'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume',
                                       'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])
    df['quote_asset_volume'] = pd.to_numeric(df['quote_asset_volume'])
    df['num_trades'] = pd.to_numeric(df['num_trades'])
    df['taker_buy_base_asset_volume'] = pd.to_numeric(df['taker_buy_base_asset_volume'])
    df['taker_buy_quote_asset_volume'] = pd.to_numeric(df['taker_buy_quote_asset_volume'])
    return df


def calculate_moving_averages(data, short_window=5, long_window=20):
    data['SMA_short'] = data['close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['close'].rolling(window=long_window).mean()


def trading_strategy(data):
    # Implement your trading strategy here based on the calculated indicators
    # For example, buy when short moving average crosses above long moving average,
    # and sell when the opposite happens.
    pass


if __name__ == "__main__":
    trading_pair = 'ETHUSD'  # Replace with the desired trading pair
    timeframe = Client.KLINE_INTERVAL_1HOUR  # Replace with the desired timeframe
    limit = 1000  # Number of data points to fetch

    historical_data = get_historical_data(trading_pair, timeframe, limit)
    calculate_moving_averages(historical_data)

    # Implement your trading strategy here
    trading_strategy(historical_data)

    # Print the historical data and indicators
    print(historical_data)
    print(historical_data['SMA_short'])
    print(historical_data['SMA_long'])

    pd = pd.DataFrame(historical_data)
    plt.plot(historical_data['close'], label='C')
    plt.plot(historical_data['open'], label='O')
    plt.plot(historical_data['high'], label='H')
    plt.plot(historical_data['low'], label='L')

    plt.plot(historical_data['SMA_short'], label='S')
    plt.plot(historical_data['SMA_long'], label='L')
    plt.legend()
    plt.show()
