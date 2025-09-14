import asyncio

async def loop(name):
    for i in range(5):
        await asyncio.sleep(1)
        print(f"{name}: {i}")

async def main():
    # Run both loops concurrently
    await asyncio.gather(loop("A"), loop("B"))

asyncio.run(main())
