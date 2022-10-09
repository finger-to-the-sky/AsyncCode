import asyncio
import time
from asyncio import Semaphore


# Написать программу, которая будет обслуживать клиентов на кассе и выводить
# время их обслуживания в зависимости от количества касс.


async def task(t: int):
    global peoples
    await asyncio.sleep(t)
    print(f'Обслуживается клиент №{peoples.index(t) + 1}')


async def get_product(semaphore: Semaphore, t: int):
    await semaphore.acquire()

    start = time.time()
    await task(t)
    end = start - time.time()

    time_on_casses = t - (end - end * 2)
    print(f'Время обслуживания: '
          f'{round((time_on_casses - time_on_casses * 2), 4)}сек')

    await asyncio.sleep(0)
    semaphore.release()


async def main(count: int, people: list):
    semaphore = Semaphore(count)
    tasks_for_cassa = [get_product(semaphore, i) for i in people]
    await asyncio.wait(tasks_for_cassa)

# Кол-во касс
count_cases = 1

# Кол-во людей len(peoples), у которых разное время для обслуживания.
clients = [1, 2, 3, 4, 5]


loop = asyncio.get_event_loop()
loop.run_until_complete(main(count_cases, clients))
