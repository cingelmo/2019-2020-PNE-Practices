from P1.Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
FOLDER = "../Session 04/"
TypeDoc = '.txt'

seq = Seq(FOLDER + 'U5' + TypeDoc)
seq.read_fasta(FOLDER + 'U5' + TypeDoc)

print("Sequence ", seq, ':', "(Length: ", seq.len(), ')', seq)
print("  Bases:", seq.seq_count())
print('  Rev:  ', seq.reverse(), '\n  Comp: ', seq.complement())
