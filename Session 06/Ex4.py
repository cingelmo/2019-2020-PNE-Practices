import termcolor


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        print('New sequence created!')

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


def print_seqs(sequence, colors):
    for seq in sequence:
        termcolor.cprint(f'Sequence {sequence.index(seq)}: (Length: {seq.len()}) {seq}', colors)


def generate_seqs(pattern, number):
    new_seq = []
    i = 0
    can_continue = True
    while can_continue:
        if i == number:
            can_continue = False
        else:
            new_seq.append(Seq(pattern * (i+1)))
            i = i + 1
    return new_seq


# --- Main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')
