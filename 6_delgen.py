

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)

        return g
    return inner


class MyException(Exception):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('.....', message)


@coroutine
def delegator(gen):
    while True:
        try:
            data = yield
            gen.send(data)

        except:
            pass



