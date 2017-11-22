import socket
import threading


class Server:
    clients = set()
    clients_lock = threading.Lock()

    def __init__(self, host, port_num):
        self.host = host
        self.port_num = port_num
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port_num))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            conn.settimeout(120)
            threading.Thread(target=self.listen_to_client, args=(conn, addr)).start()

    def listen_to_client(self, client, addr):
        with self.clients_lock:
            self.clients.add(client)
        try:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    resp = data
                    with self.clients_lock:
                        for c in self.clients:
                            c.sendall(resp)
        finally:        
            with self.clients_lock:
                self.clients.remove(client)
                client.close()

if __name__ == '__main__':
    while True:
        port = input('Port number please: ')
        try:
            port = int(port)
            break
        except ValueError:
            pass

    Server('', int(port)).listen()




















