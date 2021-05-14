import os
import asyncio
from async_file_manager import AsyncFile

async def get_python_filenames(startdir):
    for dir, _, filenames in os.walk(startdir):
        for filename in filenames:
            if filename.endswith(".py"):
                yield os.path.join(dir, filename)


async def main():
    async for f in get_python_filenames("."):
        print(f)

asyncio.run(main())