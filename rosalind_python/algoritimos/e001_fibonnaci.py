import os
class fibonnaci:
    def __init__(self,fibonacci=6):
        os.system('cls')
        self.fibonnaci_str = fibonacci
    def fibonnaci_numbers(self):
        old,new =1,1
        for itr in range(self.fibonnaci_str-1):
            new, old = old, old+new
        return new
    
    def __str__(self) -> str:
        return f'o termo na sequencia de fibbonaci no ponto {self.fibonnaci_str} é {self.fibonnaci_numbers()}'

numero_input = int(input('digite o numero que deseja gerar na sequencia de fibonnaci '))
sequencia_fibonnaci = fibonnaci(numero_input)
print(sequencia_fibonnaci)

