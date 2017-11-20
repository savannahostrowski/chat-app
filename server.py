import socket
import sys

from threading import Thread


class Server(object):
    def __init__(self, host='', port_num=8000):
        self.host = host
        self.port_num = port_num
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port_num))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            conn.settimeout(60)
            Thread(target=self.listen_to_client, args=(conn, addr))

    def listen_to_client(self, conn):
        while True:
            try:
                data = conn.recv(1024)
                if data:
                    resp = data
                    print(resp.decode())
                    conn.sendall(resp)
                else:
                    raise socket.error('Client disconnected')
            except socket.error:
                conn.close()
                return False

if __name__ == '__main__':
    while True:
        port = input('Port number please: ')
        try:
            port = int(port)
            print('Port available')
            break
        except ValueError:
            pass
    Server('', port).listen()




















