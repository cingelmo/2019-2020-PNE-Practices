from P0.Seq0 import*

FOLDER = "../Session-04/"
File = ['U5']
TypeDOC = '.txt'

print('----| Exercise 6| ----')

for element in File:
    sequence = seq_read_fasta(FOLDER + element + TypeDOC)[0:20]
    print('Gene', element, ' : ', '\nFrag: ', sequence, '\nRev : ', seq_reverse(sequence))
