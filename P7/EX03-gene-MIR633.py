import http.client
import json
import termcolor

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362', }

GENE = 'MIR633'
Server = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
Request = ENDPOINT + GENES[GENE] + PARAMS
URL = Server + Request

print()
print(f"Server: {Server}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(Server)

try:
    conn.request("GET", Request)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode()
gene = json.loads(data1)

print('Dictionary of genes!')
print(f"There are {len(GENES)} genes in the dictionary:\n")

for gen in GENES:
    termcolor.cprint(f"{gen}", "green", end="")
    print(f": {GENES[gen]}")

termcolor.cprint("Gene", 'green', end="")
print(f": {GENE}")
termcolor.cprint("Description", 'green', end="")
print(f": {gene['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {gene['seq']}")
