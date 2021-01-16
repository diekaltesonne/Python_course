import sys
import asyncio
storage = {}
class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        resp = process(data.decode())
        self.transport.write(resp.encode())


def process(data):
    comm, pay = data.split(' ', 1)
    if comm == 'put':
        s = put(pay)
        return s
    elif comm == 'get':
        s = get(pay)
        return s
    else:
        return 'error\nwrong command\n\n'

def put(data):
    name,value, time = data.split()
    if name not in storage:
        storage[name] = {}
        storage[name].update({time: value})

    else:
        storage[name].update({time: value})
    return 'ok\n\n'


def get(data):

    ky = data.strip()
    if ky == '*':
        response = 'ok\n'
        for ky, val in storage.items():
            for v in sorted(val):
                response += '%s %s %s\n' % (ky, val[v], v)
        response += '\n'
        return response
    else:
        values = storage.get(ky)
        if values:
            response = 'ok\n'
            for v in sorted(values):
                response += '%s %s %s\n' % (ky, values[v], v)
            response += '\n'
            return response
        else:
            return 'ok\n\n'


def run_server(host,port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol,host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    host, port = sys.argv[1:]
    run_server(host, port)

'''
    def data_received(self, data):
        output = "error\nwrong command\n\n"
        peername = self.transport.get_extra_info('peername')[1]
        #message = process_data(data.decode())
        message = data.decode()
        print('Data received: {!r}'.format(message))
        rm = message.split("\n").remove('')
        if  isinstance(rm, list):
            for i in message.split("\n"):
                if i.split()[0]=="put":
                    print(i)
                    output = self.upload_data(peername,i)
                    #print(data_base)
                    self.transport.write(output.encode())
                if i.split()[0]=="get":
                    output = self.data_transmitted(peername,i)
                    print(output.encode())
                    self.transport.write(output.encode())
        else:
            if str(rm).split()[0]=="put":
                print(i)
                output = self.upload_data(peername,rm)
                #print(data_base)
                self.transport.write(output.encode())
            if str(rm).split()[0]=="get":
                output = self.data_transmitted(peername,rm)
                print(output.encode())
                self.transport.write(output.encode())
        self.transport.write(output.encode())
'''
'''
    def upload_data(self,peername,data):
        data = data.split("\n")
        data = data[4:]
        print(data)

        if data_base.get(peername) == None:
            data_base[peername]=[]
            data_base[peername].append(data)
        else:
            data_base[peername].append(data)

        data = data[4:]
        print(data)
        return "ok\n\n"
'''

'''
    def data_transmitted(self,peername,data):
        #Успешный ответ от сервера:
        #ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
        output = ""
        g = data.split()
        if data_base.get(peername) == None:
            return "ok\n\n"
        else:
            if g[1] == "*":
                for i in data_base[peername]:
                    output= output+f'{i}\n'
            else:
                for i in data_base[peername]:
                    if g[1] == i.split()[0]:
                        output = output + f'{i}\n'

        print('ok\n'+output+'\n')
        return 'ok\n'+output+'\n'
'''
