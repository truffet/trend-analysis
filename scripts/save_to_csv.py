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
    header = ['Pair', '4H Change', '24H Change', 'Ratio', '4H Volume', '24H Volume', '4H Open Time', '4H Open', '4H Close', '12H Open', '12H Close', 'Interpretation']

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
                clean_data(entry['open_4h']),
                clean_data(entry['close_4h']),
                clean_data(entry['open_12h']),
                clean_data(entry['close_12h']),
                entry.get('interpretation', '')
            ]
            writer.writerow(row)

    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    ohlcv_data = [
        {
            'pair': 'BTCUSDT',
            'change_4h': 2.5,
            'change_24h': 5.0,
            'ratio': 0.5,
            'volume_4h': 1000,
            'volume_24h': 6000,
            'open_4h_time': '2021-01-01T00:00:00Z',
            'open_4h': 30000,
            'close_4h': 31000,
            'open_12h': 29000,
            'close_12h': 30500,
            'interpretation': 'positive'
        }
        # Add more data entries as needed
    ]

    save_data_to_csv(ohlcv_data)
