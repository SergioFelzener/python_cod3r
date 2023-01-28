class Pokemon:
    def __init__(self, tipo, especie, power=100, magic=0):
        self.tipo = tipo
        self.especie = especie
        self.power = power
        self.magic = magic
        
    def __str__(self):
        return f'Pokemon {self.especie, self.tipo, self.power}'
        # return 'Especie :{}\nTipo :{}\nPower = {}'.format(self.especie, self.tipo, self.power)
        
    def attack(self, attack=0):
        self.attack = attack
        if self.tipo == 'fogo':
            self.attack = 10
        self.power = self.power - attack
        
        


p1 = Pokemon('fogo', 'Chamamix')
print(p1)
print(p1.attack())
print(p1.power)
