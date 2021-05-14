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
    with open(filename) as f:
        for _ in f:
            counter += 1
    return counter

async def process_file_async(filename):
    counter = 0
    async with AsyncFile(filename) as f:
        async for _ in f:
            counter += 1
    return counter

async def main_async():
    tasks = []
    async for f in get_python_filenames("."):
        tasks.append(asyncio.create_task(process_file_async(f)))
    res = await asyncio.gather(*tasks)
    return sum(res)

async def main_sync():
    counter = 0
    async for f in get_python_filenames("."):
        counter += process_file(f)
    return counter

start = time.time()
res = asyncio.run(main_sync())
end = time.time()

print(f"sync time: {end-start}")
print(f"res = {res}")

start = time.time()
res = asyncio.run(main_async())
end = time.time()

print(f"async time: {end-start}")
print(f"res = {res}")