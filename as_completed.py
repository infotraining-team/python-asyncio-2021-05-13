import asyncio
import socket
from keyword import kwlist

"""
check if getaddrinfo returns good value for python keywords
yield.pl -> free
with.pl  -> taken
"""

def get_names():
    return (kw for kw in kwlist if len(kw) <= 5)

async def test():
    loop = asyncio.get_running_loop()
    await loop.getaddrinfo("wp.pl", None)
    try:
        await loop.getaddrinfo("asasdfasfadsfasfsaf.pl", None)
    except socket.gaierror:
        print("domain not exists")

async def fun(n):
    await asyncio.sleep(n)
    return n

async def main():
    print(list(get_names()))
    await test()
    coros = [fun(n) for n in (2, 1, 4, 0.5)]
    for coro in asyncio.as_completed(coros):
        res = await coro
        print(res)

asyncio.run(main())