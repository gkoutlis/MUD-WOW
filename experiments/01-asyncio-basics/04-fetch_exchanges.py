import asyncio
import time
import random

start=time.time()

async def fetch_price(exchange_name, delay):
    price = random.randint(60000, 70000)
    print(f"{exchange_name} Ξεκινάει request...")
    # await asyncio.sleep(delay)
    time.sleep(delay)
    print(f"{exchange_name} Τιμή: $ {price} ")
    return price

async def main():
    res = await asyncio.gather(
        fetch_price("Binance", 2),
        fetch_price("Coinbase", 3),
        fetch_price("Kraken", 1),
        fetch_price("Bitstamp", 4),
        fetch_price("OKX", 2),
    )


    print(f"o mesos oros einai: {sum(res) / len(res)}")
    print(f"Συνολικός χρόνος: {time.time() - start:.2f} sec")


asyncio.run(main())



