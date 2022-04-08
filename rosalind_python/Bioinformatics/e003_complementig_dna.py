"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""
class complementig_dna:
    def __init__(self,dna):
        self.dna_str = dna
        self.dna = self.processed()
        self.cross = {
                "A":"T",
                "T":"A",
                "G":"C",
                "C":"G"
        }
        self.reverse_dna = ''
    def processed(self):
        if self.dna_str.isalpha():
             return self.dna_str.upper()
    
    def complementig(self): 
        return self.dna[::-1]

    def cross_dna(self):
        dna = self.complementig()
        for codon in dna:
            self.reverse_dna+=self.cross[codon]
        return self.reverse_dna

    def start(self):
        self.cross_dna()

    def __str__(self):
        return f'A fita invertida fica {self.reverse_dna}'
entrada = 'AAAACCCGGT'
com = complementig_dna(entrada)
com.start()
print(com)

