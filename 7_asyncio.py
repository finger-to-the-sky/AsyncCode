# pip install aiohttp

# План:
# 1. Asyncio фреймворк для создания событийных циклов(event_loop)
# 2. Пример простой асинхронной программы времен Python 3.4
# 3. Синтаксис Async/await на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов

import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
