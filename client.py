import socket

HOST = ''
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        r = input('Enter message: ')
        s.sendall(r.encode())

        data = s.recv(1024)
        print('Received data: ' + data.decode())
