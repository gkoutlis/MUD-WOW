import asyncio
import time


async def task(name, duration):
    print(f"{name} ξεκινησε")
    time.sleep(duration)

    print(f"{name} τελειωσε ")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1),
    )

asyncio.run(main())