class Pokemon:
    def __init__(self, tipo, especie, name=None, power=100, magic=0, level=1):
        self.tipo = tipo
        self.especie = especie
        self.name = name
        self.power = power
        self.magic = magic
        self.level = level

        if name:
            self.name = name
        else:
            self.name = especie

    def __str__(self):
        return f'Pokemon Nome **{self.name}**\nSua espécie é : {self.especie}\nSeu tipo : {self.tipo}\nForça {self.power}\nMagia : {self.magic}\nLevel : {self.level}'
        # return 'Especie : {}\nTipo : {}\nPower = {}\n'.format(self.especie, self.tipo, self.power)

    def attack(self, pokemon):
        attack = 10
        print("{}\nAtacou .....{} ".format(self, pokemon))
        pokemon.power = pokemon.power - attack
        print(f'sua força de ataque foi ... {attack}')
        print('Seu força caiu para', pokemon.power)


p1 = Pokemon('Fogo', 'Chamamix')
p2 = Pokemon('Eletrico', 'Pikachu')
print(p1)
p1.attack(p2)
