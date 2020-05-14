from P0.Seq0 import *

filename = ["U5", 'ADA', 'FRAT1', 'FXN']
FOLDER = "../Session-04/"
TypeDOC = '.txt'

print('----| Exercise 3| ----')

for element in filename:
    sequence = seq_read_fasta(FOLDER + element + TypeDOC)
    print('Gene ', element, '---> Length: ', seq_len(sequence))
