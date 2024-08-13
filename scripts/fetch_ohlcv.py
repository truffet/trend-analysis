import requests
import time

def get_ohlcv(symbol, interval, limit=100):
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching OHLCV data for {symbol}: {response.status_code}")
        return []

def fetch_ohlcv_data_for_pairs(pairs):
    data = []
    for pair in pairs:
        print(f"Fetching data for {pair}...")
        ohlcv_4h = get_ohlcv(pair, '4h', limit=1)  # Fetch the last 4-hour period
        time.sleep(1)  # Delay to avoid hitting rate limit

        ohlcv_24h = get_ohlcv(pair, '4h', limit=6)  # Fetch the preceding 24-hour period
        time.sleep(1)  # Delay to avoid hitting rate limit

        if ohlcv_4h and ohlcv_24h:
            data.append({
                'pair': pair,
                'ohlcv_4h': ohlcv_4h,
                'ohlcv_24h': ohlcv_24h
            })
        else:
            print(f"Skipping {pair} due to missing data")

    return data
