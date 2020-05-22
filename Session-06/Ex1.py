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


# --- Main program
s1 = Seq("ACCGTGC")
s2 = Seq("Hello? Am I a valid sequence?")

print("Sequence 1: ", s1)
print("Sequence 2: ", s2)
