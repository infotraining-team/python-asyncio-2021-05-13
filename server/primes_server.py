import asyncio
import primes

from concurrent.futures import ProcessPoolExecutor as Pool

pool = Pool(max_workers=8)

async def primes_server(address):
    server = await asyncio.start_server(primes_handler, *address)
    addr = server.sockets[0].getsockname()
    print(f"start on {addr}")
    await server.serve_forever()

async def primes_handler(reader, writer):
    while True:
        data = await reader.read(100000)
        try:
            prime_to_test = int(data)
        except ValueError:
            continue
        ### CPU code
        ## threads - still not good
        ## result = await asyncio.to_thread(primes.primes_up_to, prime_to_test)
        ## result = primes.primes_up_to(prime_to_test)
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(pool, primes.primes_up_to, prime_to_test)
        ### CPU end
        writer.write(f'result for {prime_to_test} = {result}'.encode("utf-8"))
        await writer.drain()

    print("conn closed")
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(primes_server(("", 25000)))