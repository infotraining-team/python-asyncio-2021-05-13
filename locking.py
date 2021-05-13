import asyncio

num = 0

async def offset():
    await asyncio.sleep(1)
    return 1

async def increment():
    global num
    num += await offset()
    # a = num
    # b = await offset()
    # num = a + b

async def safe_increment(lock):
    global num
    async with lock:
        num += await offset()

async def safe_increment2():
    global num
    off = await offset()
    num += off

async def main():
    #lock = asyncio.Lock()
    tasks = []
    for i in range(10000):
        tasks.append(safe_increment2())
    await asyncio.gather(*tasks)
    print(f"num = {num}")

asyncio.run(main())