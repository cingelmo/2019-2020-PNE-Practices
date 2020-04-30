from Client0 import Client
from P1.Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session 04/"
Filename = "FRAT1"
TypeDoc = '.txt'

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

seq = Seq().read_fasta(FOLDER + Filename + TypeDoc)
bases = str(seq)
print('Gene ', Filename, ':', seq)

c.talk(f"Sending {Filename} Gene to the server, in fragments of 10 bases")
for i in range(5):
    fragment = (bases[i*10:(i+1)*10])
    print(f"Fragment {i+1}: {fragment}")
    c.talk(f"Fragment {i+1}: {fragment}")
