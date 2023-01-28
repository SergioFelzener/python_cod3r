class Pokemon:
    def __init__(self, tipo, especie, power=100, magic=0):
        self.tipo = tipo
        self.especie = especie
        self.power = power
        self.magic = magic
        
    def __str__(self):
        # return f'Pokemon {self.especie, self.tipo, self.power}'
        return 'Especie : {}\nTipo : {}\nPower = {}\n'.format(self.especie, self.tipo, self.power)
        
    def attack(self, pokemon):
        print("{}\nAtacou .....{} ".format(self, pokemon))
        pokemon.power = pokemon.power - 10
        print(pokemon)
        
        
        
        


p1 = Pokemon('Fogo', 'Chamamix')
p2 = Pokemon('Eletrico', 'Pikachu')
p1.attack(p2)


