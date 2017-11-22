import socket

HOST = ''
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('A new client has connected to the server'.encode())

    while True:
        r = input('Enter message: ')
        s.sendall(r.encode())

