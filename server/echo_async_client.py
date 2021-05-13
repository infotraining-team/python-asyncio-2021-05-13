import asyncio
import time

async def client(address):
    reader, writer = await asyncio.open_connection(*address)
    while True:
        writer.write(b'Hello from client')
        await writer.drain()
        resp = await reader.read(100000)
        print(b"got: " + resp)
        time.sleep(1)

asyncio.run(client(('localhost', 25000)))