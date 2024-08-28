import requests
import time
import hmac
import hashlib

# HashKey API credentials and endpoint
hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
hashkey_base_url = 'https://api.hashkey.com'

# Get HashKey spot market price
def get_hashkey_spot_price(symbol):
    endpoint = f'/api/v1/market/ticker/price?symbol={symbol}'
    url = hashkey_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['price'])

# Get HashKey futures market price
def get_hashkey_futures_price(symbol):
    endpoint = f'/api/v1/futures/ticker/price?symbol={symbol}'
    url = hashkey_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['price'])

# Sign request (needed for authenticated endpoints)
def sign_request(params, secret_key):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

# Place an order on HashKey
def send_hashkey_order(symbol, side, quantity, order_type='LIMIT'):
    endpoint = '/api/v1/order'
    url = hashkey_base_url + endpoint
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,  # BUY or SELL
        'type': order_type,
        'quantity': quantity,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'apiKey': hashkey_api_key
    }
    params['sign'] = sign_request(params, hashkey_secret_key)
    response = requests.post(url, data=params)
    return response.json()

# Main strategy logic
def arbitrage_strategy():
    symbol = 'BTCUSDT'
    while True:
        # Fetch spot and futures market prices
        spot_price = get_hashkey_spot_price(symbol)
        futures_price = get_hashkey_futures_price(symbol)

        # Calculate arbitrage opportunity
        threshold = 0.01  # Arbitrage threshold (1%)
        if futures_price > spot_price * (1 + threshold):
            # Buy on spot, sell on futures
            quantity = 0.001  # Trade quantity
            send_hashkey_order(symbol, 'BUY', quantity)
            send_hashkey_order(symbol, 'SELL', quantity, 'MARKET')
        elif spot_price > futures_price * (1 + threshold):
            # Buy on futures, sell on spot
            quantity = 0.001  # Trade quantity
            send_hashkey_order(symbol, 'SELL', quantity)
            send_hashkey_order(symbol, 'BUY', quantity, 'MARKET')

        # Wait before checking again
        time.sleep(60)

# Start the strategy
if __name__ == "__main__":
    arbitrage_strategy()
