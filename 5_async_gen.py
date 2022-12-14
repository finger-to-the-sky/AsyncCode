
# async on generators
import socket
from select import select


tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('read', server_socket)

        client_socket, address = server_socket.accept()
        print('Connection from ', address)

        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('read', client_socket)

        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello World\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()


def event_loop():

    while any([tasks, to_read, to_write]):
        while not tasks:

            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            # select заберет из словаря ключи

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
            # метод pop - удаляет пару из словаря, но записывает в себя значение
            # удаленной пары. То есть в tasks попал генератор

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task

        except StopIteration:
            pass


tasks.append(server())
event_loop()
