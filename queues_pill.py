import asyncio
from asyncio.exceptions import CancelledError

async def producer(q):
    for i in range(10):
        await q.put(i)
        await asyncio.sleep(0.1)
    ## finishing
    await q.put(None)

async def watcher(q, name):
    while True:
        task = await q.get()
        if task is not None:
            print(f"{name} got {task}")
            await asyncio.sleep(1)
        else:
            await q.put(None)
            break

async def main():
    q = asyncio.Queue()
    p = asyncio.create_task(producer(q))
    watchers = asyncio.gather(*[watcher(q, f"{i}") for i in range(3)])
    await p
    await watchers

asyncio.run(main())