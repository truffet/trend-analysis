# 4H/1D Trend Analysis

This project fetches cryptocurrency trading data, calculates 4-hour and 1-day percentage changes, and stores the results in a local CSV file.

## Project Structure

4h_1d_trend_analysis/
│
├── data/
│   └── __init__.py
│   └── ohlcv_data.csv
│
├── scripts/
│   ├── __init__.py
│   ├── fetch_pairs.py
│   ├── fetch_ohlcv.py
│   ├── calculate_changes.py
│   ├── save_to_csv.py
│
├── main.py
├── requirements.txt
└── README.md

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd 4h_1d_trend_analysis
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

Execute the main script to fetch data, calculate changes, and store results:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.
