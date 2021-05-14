import asyncio
from asyncio.exceptions import CancelledError

async def producer(q):
    for i in range(10):
        await q.put(i)
        await asyncio.sleep(0.1)

async def watcher(q, name):
    while True:
        task = await q.get()
        print(f"{name} got {task}")
        await asyncio.sleep(1)
        q.task_done()

async def main():
    q = asyncio.Queue()
    p = asyncio.create_task(producer(q))
    watchers = asyncio.gather(*[watcher(q, f"{i}") for i in range(3)])
    await p
    print("waiting for watchers to finish")
    await q.join()
    watchers.cancel()
    try:
        await watchers
    except CancelledError:
        print("watchers finished")

asyncio.run(main())