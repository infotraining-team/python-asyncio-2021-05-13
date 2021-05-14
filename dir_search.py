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

async def main():
    counter = 0
    async for f in get_python_filenames("."):
        counter += process_file(f)
    return counter

start = time.time()
res = asyncio.run(main())
end = time.time()

print(f"time: {end-start}")
print(f"res = {res}")
