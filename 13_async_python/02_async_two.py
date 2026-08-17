import asyncio
import time

async def brew(name):
    print(f"Brewing: {name}")
    await asyncio.sleep(2)
    # time.sleep(3)
    print(f"Brewing completed for: {name}")

async def main():
    await asyncio.gather(
        brew("Lemon"),
        brew("Ginger"),
        brew("Cardamom")
    )

asyncio.run(main())