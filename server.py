import socket

HOST = ''
PORT = 8000

# Create new socket
# AF_INET = the address families, SOCK_STREAM = socket types
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket to address
    s.bind((HOST, PORT))
    # Enable server to accept connections
    s.listen(5)
    # Accept a connection
    # Conn = new socket object usable to send and receive data on connection
    # Addr = the address bound to the socket on the other end of the connection
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # Receive data from socket in bytes (max size is 1024 at a time)
            data = conn.recv(1024)
            if not data:
                break
            # Send data to socket
            print(data.decode())
            conn.sendall(data)
        conn.close()
