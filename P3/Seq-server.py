import socket
import termcolor
from P1.Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()


print("Server configured!")

sequences = ["TCTTCCATCCCACCTCGCAGTGCCGTACCTGATTTGTGATTCCGAGGGC",
             "CAACAAACACCATCCCTCGTCCGTCCTCTTCCAAGACTAGTCCCATCCA",
             "GGCCTCCGGACCAGTAAATTAACCTCCCCCCCTCACGGCCGTGATTCCC",
             "AGCGCAACTGCATCACCATTTCCGACTCCTCACCACATTCCTATTTTGA"]
bases = ["A", "C", "T", "G"]
folder = "../Session-04/"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

while True:
    print('Waiting for clients...')
    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print('Server stopped')
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        all_lines = msg.split('\n')
        first_line = all_lines[0].strip()
        commands = first_line.split(' ')

        if len(commands) >= 2:
            cmd1 = commands[0]
            cmd2 = commands[1]
        else:
            cmd1 = msg
            cmd2 = ''

        response = ''
        if cmd1 == 'PING':
            termcolor.cprint('PING command!', 'green')
            response = 'OK!'

        elif cmd1 == "GET":
            for element in range(len(sequences)):
                if element == int(cmd2):
                    termcolor.cprint("GET", 'green')
                    response = sequences[element]

        elif cmd1 == "INFO":
            seq0 = Seq(cmd2)
            response = ""
            termcolor.cprint("INFO", 'green')
            response += f'Sequence: {cmd2}'
            response += f"Total length: {seq0.len()}"
            for element in bases:
                resp = round(seq0.count_base(element) * (100 / seq0.len()), 2)
                response += f'{element}: {seq0.count_base(element)} ( {resp}% ) \n'

        elif cmd1 == "COMP":
            seq0 = Seq(cmd2)
            termcolor.cprint("COMP", 'green')
            response = seq0.complement()

        elif cmd1 == "REV":
            seq0 = Seq(cmd2)
            termcolor.cprint("REV", 'green')
            response = seq0.reverse()

        elif cmd1 == "GENE":
            seq0 = Seq("")
            seq0 = seq0.read_fasta(folder + cmd2 + '.txt')
            termcolor.cprint("GENE", 'green')
            response = seq0.reverse()

        print(response)
        cs.send(response.encode())
        cs.close()
