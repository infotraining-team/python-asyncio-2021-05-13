import asyncio
from asyncio.tasks import sleep

async def coro(delay):
    try:
        print(f"start sleeping for {delay}")
        await asyncio.sleep(delay)
        print(f"slept for {delay}")
    except asyncio.CancelledError:
        print(f"got cancelled {delay}")

async def main():
    coros = [coro(i) for i in range(5)]
    print("launching")
    tasks = asyncio.gather(*coros)
    await asyncio.sleep(3)
    tasks.cancel()
    try:
        await tasks
    except asyncio.CancelledError:
        print("cancelled")

async def shielded():
    c = coro(4)
    task = asyncio.create_task(c)
    shielded_task = asyncio.shield(task)
    await asyncio.sleep(2)
    shielded_task.cancel()
    await task


asyncio.run(shielded())