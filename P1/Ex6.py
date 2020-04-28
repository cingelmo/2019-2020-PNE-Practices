from P1.Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")
seq0 = Seq()
seq1 = Seq("ACTGA")
seq2 = Seq("Invalid sequence")

bases = ["A", "T", "C", "G"]

for seq, value in enumerate([seq0, seq1, seq2]):
    print("Sequence ", seq, ':', "(Length: ", value.len(), ')', value)
    print("Bases:", value.seq_count())
