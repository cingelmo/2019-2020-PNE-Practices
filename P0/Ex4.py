from P0.Seq0 import *

filename = ["U5", 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
TypeDOC = '.txt'
all_bases = ["A", 'C', 'T', 'G']
FOLDER = "../Session 04/"

print('----| Exercise 4| ----')

for element in filename:
    sequence = seq_read_fasta(FOLDER + element + TypeDOC)
    print('Gene', element, ' :')
    for base in all_bases:
        print(base, seq_count_base(sequence, base))
