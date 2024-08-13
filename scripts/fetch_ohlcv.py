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
            # Use the second most recent for 4H calculations (the most recent one is unfinished)
            ohlcv_4h = [ohlcv_last_8[1]]
            
            # Use the 6 periods starting from 2024-08-12 06:00:00 to 2024-08-13 06:00:00 for 1D calculations
            ohlcv_24h = ohlcv_last_8[2:]
            
            data.append({
                'pair': pair,
                'ohlcv_4h': ohlcv_4h,
                'ohlcv_24h': ohlcv_24h
            })
        else:
            print(f"Skipping {pair} due to insufficient data")

    return data
