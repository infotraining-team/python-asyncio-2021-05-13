
###
"""
http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date_str}
table = 'A'
currency = "USD"
date_str = "2020-11-28"

"""
import asyncio
import aiohttp

async def starting_point():
    async with aiohttp.ClientSession() as s:
        async with s.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/2021-05-13") as response:
            if response.status == 200:
                print(await response.json())

asyncio.run(starting_point())

# TODO:
# parse csv (possibly async)
# get exchange rate
# rate * value = PLN
# return sum