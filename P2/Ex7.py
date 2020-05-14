from Client0 import Client
from P1.Seq1 import Seq

PRACTICE = 2
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
Filename = "FRAT1"
TypeDoc = '.txt'

IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)
seq = Seq().read_fasta(FOLDER + Filename + TypeDoc)
bases = str(seq)
print('Gene ', Filename, ':', seq)

c1.talk(f"Sending {Filename} Gene to the server, in fragments of 10 bases")
c2.talk(f"Sending {Filename} Gene to the server, in fragments of 10 bases")
for i in range(10):
    fragment = (bases[i*10:(i+1)*10])
    print(f"Fragment {i+1}: {fragment}")
    if i % 2:
        c2.talk(f"Fragment {i+1}: {fragment}")
    else:
        c1.talk(f"Fragment {(i+1)}: {fragment}")
