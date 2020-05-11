from Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
for i in range(5):
    print(c.talk(f'GET {i}'))

print("* Testing INFO...")
print(c.talk(f"INFO {seq}"))

print("* Testing COMP...")
print(c.talk(f"COMP {seq}"))

print("* Testing REV...")
print(c.talk(f"REV {seq}"))

print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    print(f"GENE {gene}")
    print(c.talk(f"GENE {gene}"))
