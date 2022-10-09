import asyncio


# 2. Создайте корутину fetch_data, которая имитирует сбор данных из сетевой базы
# данных. Предположим, что это занимает
# несколько секунд. Он должен вернуть словарь {"data":100}. Затем создайте новую
# корутину, которая считает от 10 до 1
# (используя диапазон). Используя await, выводите каждое число на экран каждые 2
# секунды.
# Наконец, создайте корутину с именем main() и одновременно запустите fetch_data
# и корутину обратного отсчета.
# Распечатайте данные, которые возвращаются из fetch_data, также считая от 10.


async def fetch_data():
    await asyncio.sleep(3)
    return {'data': 100}


async def timer():
    for i in range(-10, 1):
        i = i - i * 2
        if i % 2 == 0:
            await asyncio.sleep(2)
            print(i)


async def main():
    res = await asyncio.gather(fetch_data(), timer())
    print(f'Result: {res[0]}')

asyncio.run(main())
