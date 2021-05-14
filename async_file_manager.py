import asyncio

class AsyncFile:
    pass


async def main():
    async with AsyncFile("hello_async.py") as f:
        content = await f.read()
    print(content)

asyncio.run(main())