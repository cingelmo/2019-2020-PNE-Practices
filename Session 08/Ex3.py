import socket

IP = '127.0.0.1'
PORT = 8080

while True:
    msg = input("Message to send: ")

    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    new_socket.connect((IP, PORT))

    new_socket.send(str.encode('Hello!'))

    new_socket.close()
