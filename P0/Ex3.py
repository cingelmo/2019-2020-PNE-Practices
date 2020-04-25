from P0.Seq0 import *
filename = ["U5.txt", 'ADA.txt', 'FRAT1.txt', 'FXN.txt']
DOC = '.txt'
FOLDER = "../Session 04/"
for element in filename:
    sequence = seq_read_fasta(FOLDER + element + DOC)
    print('Gene ', element, '---> Length: ', seq_len(FOLDER + element))
