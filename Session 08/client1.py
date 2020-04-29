import socket

IP = '192.168.1.48 '
PORT = 8080

# --- We create the socket
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- Establishing the connection with the server
new_socket.connect((IP, PORT))

# --- Send data to the server
new_socket.send(str.encode('hello'))

# ---Recieve data from the server
msg = new_socket.recv(2000)
print('Message from the server: \n', msg.decode('utf-8'))

# ---Closing the connection
new_socket.close()
