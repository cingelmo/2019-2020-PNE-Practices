from P1.Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
seq0 = Seq()
seq1 = Seq("ACTGA")
seq2 = Seq("AFCTGS")

bases = ["A", "C", "G", "T"]

for seq, value in enumerate([seq0, seq1, seq2]):
    print("Sequence ", seq, ':', "(Length: ", value.len(), ')', value)
    for base in bases:
        print(base, ":", value.count_base(base), end=" ")
    print()
