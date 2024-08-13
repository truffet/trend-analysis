import sys
import os

# Add the scripts directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from fetch_pairs import get_usdt_pairs
from fetch_ohlcv import fetch_ohlcv_data_for_pairs
from calculate_changes import process_ohlcv_data
from save_to_csv import save_data_to_csv

def main():
    # Step 1: Retrieve USDT pairs
    usdt_pairs = get_usdt_pairs()
    print(f"Number of USDT pairs: {len(usdt_pairs)}")
    print(usdt_pairs[:10])  # Print the first 10 pairs to verify

    # Step 2: Fetch OHLCV data
    #ohlcv_data = fetch_ohlcv_data_for_pairs(usdt_pairs[:5])  # Limit to 5 pairs for quick inspection
    ohlcv_data = fetch_ohlcv_data_for_pairs(usdt_pairs) # full search
    
    # Step 3: Calculate changes and extract additional fields
    processed_data = process_ohlcv_data(ohlcv_data)

    # Step 4: Store results in Google Sheets
    save_data_to_csv(processed_data)

if __name__ == "__main__":
    main()