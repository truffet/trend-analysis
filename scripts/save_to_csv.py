import csv
import os
import math

def clean_data(value):
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "Infinity"
    return value

def save_data_to_csv(ohlcv_data, filename='data/ohlcv_data.csv'):
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Define the header
    header = ['Pair', '4H Change', '24H Change', 'Ratio', '4H Volume', '24H Volume', '4H Open Time', '4H Close Time', '4H Open', '4H Close', '12H Open Time', '12H Close Time', '12H Open', '12H Close', 'Interpretation']

    # Write the data to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        
        for entry in ohlcv_data:
            row = [
                entry['pair'],
                clean_data(entry['change_4h']),
                clean_data(entry['change_24h']),
                clean_data(entry['ratio']),
                clean_data(entry['volume_4h']),
                clean_data(entry['volume_24h']),
                entry['open_4h_time'],
                entry['close_4h_time'],
                clean_data(entry['open_4h']),
                clean_data(entry['close_4h']),
                entry['open_12h_time'],
                entry['close_12h_time'],
                clean_data(entry['open_12h']),
                clean_data(entry['close_12h']),
                entry.get('interpretation', '')
            ]
            writer.writerow(row)

    print(f"Data saved to {filename}")
