class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print('New sequence created!')

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

print("Sequence 1: ", s1)
print("  Length: ", s1.len())
print("Sequence 2: ", s2)
print("  Length: ", s2.len())

class Gene(Seq):
    """This class is derived from the Seq Class
    All the objects of class Gene will inherit
    the methods from the Seq class
    """
    def __init__(self, strbases, name=''):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

print('Sequence 1: ', s1)
print('Gene: ', g)