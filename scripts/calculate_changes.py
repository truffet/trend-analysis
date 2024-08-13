def calculate_changes(ohlcv_4h, ohlcv_24h):
    open_4h = float(ohlcv_4h[0][1])  # Open price of the last 4-hour period
    close_4h = float(ohlcv_4h[-1][4])  # Close price of the last 4-hour period
    open_4h_time = ohlcv_4h[0][0]  # Open time of the last 4-hour period
    
    open_24h = float(ohlcv_24h[0][1])  # Open price of the first 4-hour period within the 24-hour period
    close_24h = float(ohlcv_24h[-1][4])  # Close price of the last 4-hour period within the 24-hour period
    
    open_12h = float(ohlcv_24h[3][1])  # Open price of the 4th 4-hour period within the 24-hour period
    close_12h = float(ohlcv_24h[3][4])  # Close price of the 4th 4-hour period within the 24-hour period
    
    change_4h = (close_4h - open_4h) / open_4h * 100  # 4H % Change
    change_24h = (close_24h - open_24h) / open_24h * 100  # 1D % Change
    ratio = change_4h / change_24h if change_24h != 0 else float('inf')  # Ratio of 4H % to 1D %
    
    volume_4h = sum([float(candle[5]) for candle in ohlcv_4h])  # Sum of volumes for the last 4-hour period
    volume_24h = sum([float(candle[5]) for candle in ohlcv_24h])  # Sum of volumes for the 24-hour period
    
    return change_4h, change_24h, ratio, volume_4h, volume_24h, open_4h_time, open_4h, close_4h, open_12h, close_12h

def process_ohlcv_data(ohlcv_data):
    for entry in ohlcv_data:
        ohlcv_4h = entry['ohlcv_4h']
        ohlcv_24h = entry['ohlcv_24h']
        change_4h, change_24h, ratio, volume_4h, volume_24h, open_4h_time, open_4h, close_4h, open_12h, close_12h = calculate_changes(ohlcv_4h, ohlcv_24h)
        entry['change_4h'] = change_4h
        entry['change_24h'] = change_24h
        entry['ratio'] = ratio
        entry['volume_4h'] = volume_4h
        entry['volume_24h'] = volume_24h
        entry['open_4h_time'] = open_4h_time
        entry['open_4h'] = open_4h
        entry['close_4h'] = close_4h
        entry['open_12h'] = open_12h
        entry['close_12h'] = close_12h

    return ohlcv_data
