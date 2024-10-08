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
        
        # Fetch the last 8 completed 4-hour periods
        ohlcv_last_8 = get_ohlcv(pair, '4h', limit=8)
        time.sleep(1)  # Delay to avoid hitting rate limit

        if len(ohlcv_last_8) == 8:
            # Use the most recent completed 4-hour period for 4H calculations
            ohlcv_4h = [ohlcv_last_8[-2]]
            
            # Use the oldest 6 of the last 8 for 1D (24 hours) calculations
            ohlcv_24h = ohlcv_last_8[:6]
            
            data.append({
                'pair': pair,
                'ohlcv_4h': ohlcv_4h,
                'ohlcv_24h': ohlcv_24h
            })
        else:
            print(f"Skipping {pair} due to insufficient data")

    return data
