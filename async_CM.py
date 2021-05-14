with open("async_CM.py") as f:
    content = f.read()

#print(content)

import asyncio

class asyncCM:
    def __init__(self, params):
        self.params = params

    async def __aenter__(self):
        print(f"entering CM with {self.params}")
        return self

    async def async_method(self):
        self.fun()
        print("the method")

    def fun(self):
        ## await self.async_method() forbidden
        print("just fun")

    async def __aexit__(self, ext, exc, tb):
        print("cleaning")

async def main():
    async with asyncCM("param") as c:
        await c.async_method()
        c.fun()

asyncio.run(main())

