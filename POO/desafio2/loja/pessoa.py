MAIOR_DE_IDADE = 18    # definindo constante conforme padrao (python nao tem constante)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade})'
    
    def is_adulto(self):
       return (self.idade or 0) > MAIOR_DE_IDADE
   
   