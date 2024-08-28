import requests
import time
import asyncio

# HashKey API credentials and other constants
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://api.hashkey.com'
FEE_RATE = 0.002  # Example transaction fee rate

def get_order_book(pair):
    url = f"{BASE_URL}/api/v1/market/orderbook?symbol={pair}"
    response = requests.get(url)
    return response.json()

async def create_order(pair, side, price, quantity):
    # Asynchronous order creation with authentication and signing
    pass

async def arbitrage_strategy():
    spot_pair = 'BTCUSDT'
    futures_pair = 'BTCUSDT_PERP'
    
    spot_data = get_order_book(spot_pair)
    futures_data = get_order_book(futures_pair)
    
    spot_price = float(spot_data['asks'][0]['price'])
    futures_price = float(futures_data['bids'][0]['price'])
    
    threshold = spot_price * (1 + FEE_RATE + 0.001)  # Including fee and a small margin
    
    if futures_price > threshold:
        # Execute arbitrage
        await asyncio.gather(
            create_order(spot_pair, 'buy', spot_price, 1),
            create_order(futures_pair, 'sell', futures_price, 1)
        )

async def main():
    while True:
        await arbitrage_strategy()
        time.sleep(5)

# Run the main event loop
asyncio.run(main())
