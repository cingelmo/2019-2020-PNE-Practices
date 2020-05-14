from Client0 import Client
from P1.Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
Filename = "U5"
TypeDoc = '.txt'

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

s = Seq().read_fasta(FOLDER + Filename + TypeDoc)

c.debug_talk(f"Sending {Filename} Gene to the server")
c.debug_talk(str(s))
