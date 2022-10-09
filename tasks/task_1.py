import asyncio


# 1. Создайте 3 корутины с именами t1, t2 и t3. Каждая корутина должна
# распечатать имя корутины.
# Вызовите/запустите первую корутину и с помощью await сначала распечатайте t3,
# затем распечатайте t2 и t1 последним.

async def t1():
    await t2()

    print('t1')


async def t2():
    await t3()
    print('t2')


async def t3():
    print('t3')

asyncio.run(t1())
