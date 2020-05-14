from P0.Seq0 import*

FOLDER = "../Session-04/"
Filename = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
TypeDOC = '.txt'
bases = ['A', 'C', 'G', 'T']

print('----| Exercise 8| ----')
i = 0
for element in Filename:
    sequence = seq_read_fasta(FOLDER + element + TypeDOC)
    Dictionary_bases = seq_count(sequence)
    Amount_bases = list(Dictionary_bases.values())
    Most_freq = max(Amount_bases)
    print('Gene: ', element, 'Most frequent base: ', bases[Amount_bases.index(Most_freq)])
