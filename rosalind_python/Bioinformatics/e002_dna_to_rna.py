"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

"""
class  DnaToRna:
    def __init__(self,dna):
        self.dna_input = dna
        self.dna = self.dna_treatment()
    
    def dna_treatment(self):
        if self.dna_input.isalpha():
            return self.dna_input.upper()

    def translator_for_rna(self):
        rna = self.dna.replace('T',"U")
        return rna 

transletor = DnaToRna('GATGGAACTTGACTACGTAAATT')
print(transletor.translator_for_rna())
