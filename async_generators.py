import asyncio

async def agen(n):
    while n >= 0:
        await asyncio.sleep(0.1)
        yield n
        n -= 1

class Counter:
    def __init__(self, count):
        self.c = count

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.c > 0:
            await asyncio.sleep(0.1)
            self.c -= 1
            return self.c
        else:
            raise StopAsyncIteration

async def main():
    async for i in agen(5):
        print(i)

    async for i in Counter(4):
        print(f"c = {i}")

    print([i async for i in agen(4)])

asyncio.run(main())