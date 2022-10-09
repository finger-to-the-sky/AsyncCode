# корутины - сопрограммы
# По сути это генераторы, которые в процессе работы могут принимать из вне какие
# то данные


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)

        return g
    return inner


def subgen():
    x = 'sfsdfs'
    message = yield x
    print('Subgen received', message)


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

