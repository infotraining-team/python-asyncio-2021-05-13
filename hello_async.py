import asyncio

async def coro():
    await asyncio.sleep(1)
    print("Hello world")
    return 42

res = asyncio.run(coro())
print(res)

#print(type(coro))
#print(type(coro()))
