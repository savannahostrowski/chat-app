import socket
import threading


class Server:
    def __init__(self, host, port_num):
        self.host = host
        self.port_num = port_num
        # object to store the active clients so we can broadcast to them
        self.clients = set()
        self.clients_lock = threading.Lock()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port_num))

    def listen(self):
        self.sock.listen(5)
        with self.clients_lock:
            print('Acquired lock')
            while True:
                client, addr = self.sock.accept()
                self.clients.add(client)
                threading.Thread(target=self.listen_and_broadcast, args=(client, addr)).start()

    def listen_and_broadcast(self, client, address):
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                for client in self.clients:
                    client.send(data)
            except socket.error:
                client.close()
                return False


if __name__ == '__main__':
    while True:
        port = input('Port number please: ')
        try:
            port = int(port)
            break
        except ValueError:
            pass

    Server('', int(port)).listen()





