import asyncio
import time

def sync_func(n):
    print(f"sync start {n}")
    time.sleep(1)
    print(f"continuing {n}")
    time.sleep(1)
    print(f"finishing {n}")
    return n

# res = [sync_func(1), sync_func(2)]
# print(res)

async def async_func(n):
    print(f"async start {n}")
    await asyncio.sleep(1)
    print(f"continuing {n}")
    await asyncio.sleep(1)
    print(f"finishing {n}")
    return n

async def main():
    ## non-blocking
    tasks = asyncio.gather(async_func(1), async_func(2), async_func(3))
    t1 = asyncio.create_task(async_func(4))
    ## block until finished
    print("waiting for tasks")
    await asyncio.sleep(0)
    print("after short wait")
    res = await tasks
    await t1
    print(res)

asyncio.run(main())
