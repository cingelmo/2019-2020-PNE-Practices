import socket
import termcolor
'''from P1.Seq1 import Seq'''

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.listen()

print("SEQ server configured!")

while True:
    try:
        print('Waiting for clients...')
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print('Server is done')
        ls.close()
        exit()

    else:
        # ---Step 5: Receiving information
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        all_lines = msg.split('\n')
        line0 = all_lines[0].strip()
        cmd = line0.split(' ')[0]

        if cmd == 'PING':
            termcolor.cprint('PING command!', 'green')
            response = 'OK!'

        else:
            print(f'From server: ', end='')
            # --Step 6: Send a response message to the client
            response = 'ECHO: ' + msg + '\n'

            cs.send(response.encode())
            cs.close()
