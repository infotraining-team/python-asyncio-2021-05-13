
###
"""
http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date_str}
table = 'A'
currency = "USD"
date_str = "2020-11-28"

"""
import asyncio
import aiohttp
import dataclasses
import datetime

@dataclasses.dataclass
class Input:
    date : datetime.date
    currency : str
    amount : float

async def parse_tansaction(date_currency_q, filename):
    with open(filename) as f:
        for line in f:
            date_str, currency, amount = line.split(" ; ")
            await date_currency_q.put(Input(datetime.datetime.strptime(date_str, "%d-%m-%Y"),
                                            currency,
                                            float(amount)))
        await date_currency_q.put(None)

async def get_json_from_url(date, currency):
    url_base = 'http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date_str}'
    correct_answer = False
    table = "A"
    while not correct_answer:
        date_str = date.strftime("%Y-%m-%d")
        async with aiohttp.ClientSession() as session:
            async with session.get(url_base.format(**locals())) as response:
                if response.status == 200:
                    correct_answer = True
                    result = await response.json()
                elif response.status == 404:
                    date = date - datetime.timedelta(1)
                else:
                    raise RuntimeError(f"Invalid status of http response. Status: {response.status} ")
    return result

async def get_json(date_currency_q, json_q):
    while True:
        input = await date_currency_q.get()
        if input is not None:
            json = await get_json_from_url(input.date, input.currency)
            await json_q.put((json, input.amount))
        else:
            await date_currency_q.put(None)
            await json_q.put(None)
            return

async def parse_json(json_q):
    total = 0
    while True:
        input = await json_q.get()
        if input is not None:
            json, amount = input
            total += amount * json['rates'][0]['mid']
        else:
            break
    return total

async def main(filename):
    date_currency_q = asyncio.Queue()
    json_q = asyncio.Queue()
    #value_q = asyncio.Queue()
    tasks = []
    tasks.append(asyncio.create_task(parse_tansaction(date_currency_q, filename)))
    tasks.append(asyncio.create_task(get_json(date_currency_q, json_q)))
    tasks.append(asyncio.create_task(get_json(date_currency_q, json_q)))
    tasks.append(asyncio.create_task(get_json(date_currency_q, json_q)))
    tasks.append(asyncio.create_task(parse_json(json_q)))
    res = await asyncio.gather(*tasks)
    return res[-1]

if __name__ == "__main__":
    res = asyncio.run(main("currency/transactions.csv"))
    print(f"total = {res}")

# TODO:
# parse csv (possibly async)
# get exchange rate
# rate * value = PLN
# return sum