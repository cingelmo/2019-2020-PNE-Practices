import http.client


SERVER = "localhost"
PORT = 8080
conn = http.client.HTTPConnection(SERVER, PORT)


print("Test report example:")
print("====================")
print("")
print("---> listSpecies endpoint")

print("**** TEST 1: *****")
print("")
conn.request("GET", "/listSpecies?limit=10")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /listSpecies?limit=10")
print("* Output: ")
print(data1)

print("**** TEST 2: ****")
print("")
conn.request("GET", "/listSpecies")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /listSpecies")
print("* Output: ")
print(data1)

print("**** TEST 3: *****")
print("")
conn.request("GET", "/listSpecies?limit=10&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /listSpecies?limit=10&json=1")
print("* Output: ")
print(data1)

print("")
print("---> karyotype endpoint")

print("***** TEST 1: *****")
print("")
conn.request("GET", "/karyotype?specie=homo_sapiens")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /karyotype?specie=homo_sapiens")
print("* Output: ")
print(data1)

print("**** TEST 2: *****")
print("")
conn.request("GET", "/karyotype?spec=12")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /karyotype?spec=12")
print("* Output: ")
print(data1)

print("**** TEST 3: *****")
print("")
conn.request("GET", "/karyotype?spec=")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /karyotype?spec=")
print("* Output: ")
print(data1)

print("")
print("---> chromosomeLenght endpoint")

print("**** TEST 1: *****")
print("")
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /chromosomeLength?specie=mouse&chromo=18")
print("* Output: ")
print(data1)

print("**** TEST 2: *****")
print("")
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /chromosomeLength?specie=mouse&chromo=18&json=1")
print("* Output: ")
print(data1)


print("")
print("---> geneSeq endpoint")

print("***** TEST 1: *****")
print("")
conn.request("GET", "/geneSeq?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneSeq?gene=FRAT1")
print("* Output: ")
print(data1)

print("***** TEST 2: *****")
print("")
conn.request("GET", "/geneSeq?gene=")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneSeq?gene=")
print("* Output: ")
print(data1)

print("***** TEST 3: *****")
print("")
conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneSeq?gene=FRAT1&json=1")
print("* Output: ")
print(data1)


print("")
print("---> geneInfo endpoint")

print("**** TEST 1: ****")
print("")
conn.request("GET", "/geneInfo?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneInfo?gene=FRAT1")
print("* Output: ")
print(data1)

print("**** TEST 2: ****")
print("")
conn.request("GET", "/geneInfo?gene=12")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneInfo?gene=12")
print("* Output: ")
print(data1)

print("**** TEST 3: ****")
print("")
conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneInfo?gene=FRAT1&json=1")
print("* Output: ")
print(data1)


print("")
print("---> geneCalc endpoint")


print("**** TEST 1: *****")
print("")
conn.request("GET", "/geneCalc?gene=FRAT1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneCalc?gene=FRAT1")
print("* Output: ")
print(data1)

print("**** TEST 2: *****")
print("")
conn.request("GET", "/geneCalc?gene=")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneCalc?gene=")
print("* Output: ")
print(data1)

print("**** TEST 3: *****")
print("")
conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneCalc?gene=FRAT1&json=1")
print("* Output: ")
print(data1)


print("")
print("---> geneList endpoint")

print("**** TEST 1:")
print("")
conn.request("GET", "/geneList?chromo=4&start=0&end=398000")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneList?chromo=4&start=0&end=398000")
print("* Output: ")
print(data1)

print("**** TEST 2: ****")
print("")
conn.request("GET", "/geneList?chromo=&stat=&end=")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneList?chromo=&stat=&end=")
print("* Output: ")
print(data1)

print("**** TEST 3: ****")
print("")
conn.request("GET", "/geneList?chromo=4&start=0&end=398000&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /geneList?chromo=4&start=0&end=398000&json=1")
print("* Output: ")
print(data1)

print("")
print("---> NON EXISTENT endpoint")

print("**** TEST 1: *****")
print("")
conn.request("GET", "/coronavirus")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
print("* Input: ")
print("GET /coronavirus")
print("* Output: ")
print(data1)