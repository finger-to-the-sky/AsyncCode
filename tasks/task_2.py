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
    for i in range(10):
        print({'data': 100})
        await asyncio.sleep(2)


async def back_counter():
    for i in range(-10, 0):
        t = i - i * 2

        print(t)
        await asyncio.sleep(2)


async def main():
    task1 = asyncio.create_task(back_counter())
    task2 = asyncio.create_task(fetch_data())
    await asyncio.gather(task1, task2)

asyncio.run(main())
