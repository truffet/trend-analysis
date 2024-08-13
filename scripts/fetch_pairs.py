import requests

def get_usdt_pairs():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pairs = [item['symbol'] for item in response.json() if item['symbol'].endswith('USDT')]
        return pairs
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []
