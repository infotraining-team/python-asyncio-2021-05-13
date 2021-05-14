import os
import asyncio
import time
from async_file_manager import AsyncFile

async def get_python_filenames(startdir):
    for dir, _, filenames in os.walk(startdir):
        for filename in filenames:
            if filename.endswith(".py"):
                yield os.path.join(dir, filename)

def process_file(filename):
    counter = 0
    with open(filename, encoding="utf-8") as f:
        for _ in f:
            counter += 1
    return counter

async def process_file_async(filename):
    counter = 0
    async with AsyncFile(filename) as f:
        content = await f.read()
        counter += len(content.splitlines())
        #async for _ in f:
        #    counter += 1
    return counter

async def producer(q, path):
    async for f in get_python_filenames(path):
        await q.put(f)
    await q.put(None)

async def consumer(q):
    counter = 0
    while True:
        filename = await q.get()
        if filename is not None:
            lines = await process_file_async(filename)
            counter += lines
        else:
            await q.put(None)
            return counter

async def main_async(path):
    q = asyncio.Queue(100)
    tasks = [consumer(q) for i in range(32)]
    await producer(q, path)
    res = await asyncio.gather(*tasks)
    return sum(res)

async def main_sync(path):
    counter = 0
    async for f in get_python_filenames(path):
        counter += process_file(f)
    return counter

path = "."

start = time.time()
res = asyncio.run(main_sync(path))
end = time.time()

print(f"sync time: {end-start}")
print(f"res = {res}")

start = time.time()
res = asyncio.run(main_async(path))
end = time.time()

print(f"async time: {end-start}")
print(f"res = {res}")