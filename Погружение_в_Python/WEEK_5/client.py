import socket
import time

class Client():

    """docstring for Client."""
    def __init__(self,HOST,PORT,timeout = None):
        self.sock = socket.create_connection((HOST,PORT),timeout)
        # self.HOST = HOST
        # self.PORT = PORT
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.create_connection(address[, timeout[, source_address]])
        # self.sock.settimeout(timeout)

        # self.sock.connect((HOST, PORT))
    # def put(self,key,value,timestamp = None):
    #     if timestamp is None:
    #         self.socket.send(('put<{key}><{value}><{timestamp}>\n'.format(key=key,value=value,timestamp = str(int(time.time())))).encode("utf-8"))
    #     else:
    #         self.socket.send(('put<{key}><{value}><{timestamp}>\n'.format(key=key,value=value,timestamp = timestamp)).encode("utf-8"))
    #     while True:
    #         data = self.socket.recv(1024)
    #         if not data:
    #             break
    #     if data.decode("utf8")=="error\nworngcommand\n\n":
    #         raise ClientError
    #
    # def get(self,key):
    #     self.socket.sendall(('get<{key}>\n'.format(key=key)).encode('utf-8'))
    #     while True:
    #         data = self.socket.recv(1024)
    #         if not data:
    #             break
    #     print('Received', repr(data))
    #     return data.decode("utf8")

    def put(self, key, value, timestamp=int(time.time())):
        message = f'put {key} {float(value)} {timestamp}\n'
        reply = self.send(message)

    def get(self, key):
        message = f'get {key}\n'
        reply = self.send(message)
        reply = self.codum2(reply)
        return(reply)

    def codum(self,reply):
        d = {}
        repl = reply.split("\n")
        for i in repl:
            k = i.split()
            if (len(k) == 1) or (len(k) == 0) :
                continue
            key, *value = k
            if d.get(key) == None:
                d[key] =[]
                d[key].append(tuple([int(value[1]),float(value[0])]))
            else:
                d[key].append(tuple([int(value[1]),float(value[0])]))
        for key in d:
            d[key] =sorted(d[key], key=lambda range: range[0])
        return d

    def codum2(self,reply):
        d = {}
        repl = reply.split("\n")
        for i in repl:
            k = i.split()
            if (len(k) == 1) or (len(k) == 0) :
                continue
            key, *value = k
            if d.get(key) == None:
                d[key] =[]
                d[key].append(tuple([int(value[1]),float(value[0])]))
            else:
                d[key].append(tuple([int(value[1]),float(value[0])]))
        return d

    def send(self, mess):
        try:
            self.sock.sendall(mess.encode('utf-8'))
            reply = self.sock.recv(1024)
        except Exception:
            raise ClientError
        return reply.decode('utf-8')

    # def __del__(self):
    #     self.sock.close()

class ClientError(Exception):
    pass
