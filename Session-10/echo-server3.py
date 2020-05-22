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
list_storing = []
while True:
    try:
        # --- Step 4: Wait for the client to connect
        print('Waiting for clients to connect')
        (cs, client_ip_port) = ls.accept()
        list_storing.append(client_ip_port)
        num_connection += 1
        print(f"CONNECTION {num_connection} Client IP,PORT: ({client_ip_port}")

        if num_connection == 5:
            print(f"The following clients have connected to the server:")
            for i, port in enumerate(list_storing):
                print(f"Client {i+1}: {port}")

    except KeyboardInterrupt:
        print('Server is done')
        ls.close()
        exit()

    else:
        # ---Step 5: Receiving information
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f'From server: ', end='')
        termcolor.cprint(msg)
        # --Step 6: Send a response message to the client
        response = 'ECHO: ' + msg + '\n'
        cs.send(response.encode())

        cs.close()
