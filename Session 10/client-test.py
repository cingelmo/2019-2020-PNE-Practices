from P2.Client0 import Client

IP = "127.0.0.1"
PORT = 8080

for index in range(0, 5):
    c = Client(IP, PORT)
    c.debug_talk(f" Message {index}")
