import socket
import sys

HOST = "127.0.0.1"
PORT = 1700


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for line in sys.stdin:
        s.sendall(line.encode())
        data = s.recv(1024)
        print(data.decode())
