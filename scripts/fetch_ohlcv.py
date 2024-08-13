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
        
        # Fetch the last 3 completed 4-hour periods (we'll use the oldest of the last 2 for 4H)
        ohlcv_last_3 = get_ohlcv(pair, '4h', limit=3)
        time.sleep(1)  # Delay to avoid hitting rate limit
        
        # Fetch the last 8 completed 4-hour periods (we'll use the oldest 6 of the last 8 for 1D)
        ohlcv_last_8 = get_ohlcv(pair, '4h', limit=8)
        time.sleep(1)  # Delay to avoid hitting rate limit

        if len(ohlcv_last_3) == 3 and len(ohlcv_last_8) == 8:
            # Use the oldest of the last 3 for 4H calculations (excluding the most recent one)
            ohlcv_4h = [ohlcv_last_3[1]]
            
            # Use the oldest 6 of the last 8 for 1D calculations (excluding the most recent 2)
            ohlcv_24h = ohlcv_last_8[:6]
            
            data.append({
                'pair': pair,
                'ohlcv_4h': ohlcv_4h,
                'ohlcv_24h': ohlcv_24h
            })
        else:
            print(f"Skipping {pair} due to insufficient data")

    return data
