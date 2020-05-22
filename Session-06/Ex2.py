class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases

        bases = ['A', 'C', 'G', 'T']
        for element in strbases:
            if element not in bases:
                print('ERROR!!')
                self.strbases = 'ERROR'
                return

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(sequence):
    for seq in sequence:
        print("Sequence ", sequence.index(seq), ':', "(Length: ", seq.len(), ')', seq)


# --- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)
