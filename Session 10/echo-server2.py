import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.listen()

print("The server is configured!")

num_connection = 0
while True:
    try:
        # --- Step 4: Wait for the client to connect
        print('Waiting for clients to connect')
        (cs, client_ip_port) = ls.accept()
        num_connection += 1
        print(f"CONNECTION {num_connection} Client IP,PORT: ({client_ip_port}")
    except KeyboardInterrupt:
        print('Server is done')
        ls.close()
        exit()

    else:
        # ---Step 5: Receiving information
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f'Received message: ', end='')
        termcolor.cprint(msg, "green")
        # --Step 6: Send a response message to the client
        response = 'ECHO: ' + msg + '\n'
        cs.send(response.encode())

        cs.close()
