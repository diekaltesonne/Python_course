import asyncio

class ClientServerProtocol(asyncio.Protocol):
    global data_base
    data_base = {}

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport


    def data_received(self, data):
        output = "error\nwrong command\n\n"
        peername = self.transport.get_extra_info('peername')[1]
        #message = process_data(data.decode())
        message = data.decode()
        print('Data received: {!r}'.format(message))
        #print(message.split()[0])
        for i in message.split("\n"):
            print(i)

        if message.split()[0]=="put":
            output = self.upload_data(message)
            self.transport.write(output.encode())
            print(data_base)

        if message.split()[0]=="get":
            output = self.data_transmitted(message)
            print(output.encode())
            self.transport.write(output.encode())

        self.transport.write(output.encode())

        #print('Close the client socket')
        #self.transport.close()

    def upload_data(self,data):
        data = data[4:]
        print(data)
        data_base.append(data)
        print(data)
        return "ok\n\n"


    def data_transmitted(self, data):
        #Успешный ответ от сервера:
        #ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
        output = ""
        g = data.split()
        #print(g[1])
        # if data_base.get(peername) == None:
        #     return "ok\n\n"
        # else:
        #
        #     if g[1] == "*":
        #         for i in data_base[peername]:
        #             output= output+f'{i}\n'
        #     else:
        #         for i in data_base[peername]:
        #             if g[1] == i.split()[0]:
        #                 output = output + f'{i}\n'

        if g[1] == "*":
            for i in data_base:
                output= output+f'{i}\n'
        else:
            for i in specdatabase:
                if g[1] == i.split()[0]:
                    output = output + f'{i}\n'


        print  'ok\n'+output+'\n'
        return 'ok\n'+output+'\n'


loop = asyncio.get_event_loop()
coro = loop.create_server(ClientServerProtocol,'127.0.0.1', 8888)

server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

'''
class server(ClientServerProtocol):
    def run_server(HOST,PORT):
        loop = asyncio.get_event_loop()
        coro = loop.create_server(ClientServerProtocol,'127.0.0.1', 8181)
        server = loop.run_until_complete(coro)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
'''

'''
@asyncio.coroutine
def _send_messages(self):
    """ Send messages to the client as they become available. """
    yield from self._ready.wait()
    print("Ready!")
    while True:
        data = yield from self.queue.get()
        self.transport.write(data.encode('utf-8'))
        print('Message sent: {!r}'.format(message))
'''
