import asyncio

class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.file = await asyncio.to_thread(open, self.filename, encoding="utf8")
        return self

    async def __aexit__(self, ext, exc, tb):
        await asyncio.to_thread(self.file.close)

    async def read(self):
        return await asyncio.to_thread(self.file.read)

    async def __aiter__(self):
        while True:
            line = await asyncio.to_thread(self.file.readline)
            if line:
                #line = line.encode('utf-8')
                yield line
            else:
                break


async def main():
    cm = AsyncFile("hello_async.py") ## __init__
    async with cm as f:              ## __aenter__
        content = await f.read()
    print(content)

if __name__ == "__main__":
    asyncio.run(main())