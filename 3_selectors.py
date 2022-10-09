
# work with module selectors

import socket
import selectors


selector = selectors.DefaultSelector()
# DefaultSelector - возвращает системную прорамму для мониторинга


def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ,
                      data=accept_connection)
    # register - регистрирует пререданные в него данные сокет, собитие,
    # обработка данных


def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    print('Connection from ', address)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ,
                      data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)
        # вызвали сокет и передали его в функцию для обработки


if __name__ ==  '__main__':
    server()
    event_loop()
