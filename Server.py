import socket

HOST='127.0.0.1'
PORT=1700

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen(1)

print("Start listenning on {}:{}".format(HOST,PORT))
while 1:

    print("Waiting for new connection...")
    client_socket, client_address=server_socket.accept()
    print("Accepted new connection")
    while 1:
        try:
            data =client_socket.recv(1024)
            if data:
                client_socket.send(data)
                continue
        except Exception as reason:
            print("client connection closed: {}".format(reason))
        client_socket.close()
        break
    pass
