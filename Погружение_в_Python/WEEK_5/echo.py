# -------- Эхо-сервер, обрабатывающий "одновременно" несколько клиентов -------
#              Обработка клиентов осуществляется функцией select

import select
import json
from socket import socket, AF_INET, SOCK_STREAM


def parse(data):
    """
    преобразует данные из байт-строки json в словарь,
    либо из словаря в байт-строку json
    использовать при каждой отправке/приеме данных
    :param data:
    :return:
    """
    if type(data) is bytes:
        return json.loads(data.decode('utf-8'))
    else:
        return json.dumps(data).encode('utf-8')


def read_requests(r_clients, all_clients):
    ''' Чтение запросов из списка клиентов
    '''
    responses = {}      # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:

            bdata = sock.recv(1024)
            data = parse(bdata)
            responses[sock] = data
            print('r --> ', [(c.fileno(), c.getpeername()[1]) for c in r_clients])
            print('\n', 'клиент {} пишет в {}'.format(data['from'], data['to']), end=': ')

        except:
            print('Клиент r {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    ''' Эхо-ответ сервера клиентам, от которых были запросы
    '''

    for sock in w_clients:
        if sock in requests:
            try:

                # Подготовить и отправить ответ сервера
                message = {'message from': requests[sock]['from'], 'text': requests[sock]['message']}
                print(message)
                bmessage = parse(message)

                sock.send(bmessage)
                print('w --> ', [(c.fileno(), c.getpeername()[1]) for c in w_clients])
                print('requests --> ', {requests})

            except:                 # Сокет недоступен, клиент отключился
                print('Клиент w {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def mainloop():
    ''' Основной цикл обработки запросов клиентов
    '''
    address = ("127.0.0.1", 8888)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)   # Таймаут для операций с сокетом
    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass                     # timeout вышел
        else:
            print("Получен запрос на соединение от {}".format(addr[1]))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)

            except:
                pass            # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)      # Сохраним запросы клиентов

            write_responses(requests, w, clients)     # Выполним отправку ответов клиентам


print('Эхо-сервер запущен!')
mainloop()
