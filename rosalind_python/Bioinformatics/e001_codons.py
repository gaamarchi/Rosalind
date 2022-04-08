class count_dna:

  def __init__(self,dna_input):
    self.dna_input= dna_input
    self.count={  'A':0,
                  'C':0,
                  'G':0,
                  'T':0
                  }
    self.processed_dna= self.dna_treatment()
  
  def count_nucleotide(self):
      self.dna_treatment()
      for nucleotide  in self.processed_dna:
          self.count[nucleotide]=self.count[nucleotide]+1
      return self.count

  def dna_treatment(self):
    if self.dna_input.isalpha():
        processed_dna = self.dna_input.upper().replace(' ','')
        return processed_dna
    
    else:
      print('input Error, just letters')


contador = count_dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
print(contador.count_nucleotide())