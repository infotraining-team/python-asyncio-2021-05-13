import asyncio

class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        return self

    async def __aexit__(self, ext, exc, tb):
        pass

    async def read(self):
        return None

async def main():
    async with AsyncFile("hello_async.py") as f:
        content = await f.read()
    print(content)

if __name__ == "__main__":
    asyncio.run(main())