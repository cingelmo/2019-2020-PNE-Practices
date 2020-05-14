from P1.Seq1 import Seq

FOLDER = "../Session-04/"
Filename = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
TypeDOC = '.txt'
bases = ['A', 'C', 'G', 'T']

print('----| Practice 1, Exercise 10| ----')
i = 0

for element in Filename:
    seq = Seq()
    seq.read_fasta(FOLDER + element + TypeDOC)
    Dictionary_bases = seq.seq_count()
    Amount_bases = list(Dictionary_bases.values())
    Most_freq = max(Amount_bases)
    print('Gene ', element, ': Most frequent base: ', bases[Amount_bases.index(Most_freq)])
