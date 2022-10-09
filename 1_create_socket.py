
# work with module socket, create connection

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - ipv4, SOCK_STREAM - tcp

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# SOL_SOCKET - socket level, SO_REUSEADDR - переиспользование адреса, true

server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    # accept() - принимает подключения. Читает данные из входящего буфера
    # Он возвращает кортеж с килентским сокетом и адресом. accept - ждет пока
    # кто то подключиться к сокету.

    print('Before accept()')
    client_socket, address = server_socket.accept()
    print('Connection from ', address)

    while True:
        # recv - выделяет размер буфера для клиентского сокета, который
        # принимает сообщения

        print('Before recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            # send - работает до тех пор пока не клиентский буфер не очиститься

            response = 'Hello World\n'.encode()
            client_socket.send(response)
            client_socket.close()

