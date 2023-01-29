class Pokemon:
    def __init__(self, especie, name=None, power=100, magic=0, level=1):
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
        return f'Pokemon Nome **{self.name}**\nSua espécie é : {self.especie}\nForça {self.power}\nMagia : {self.magic}\nLevel : {self.level}'
        # return 'Especie : {}\nTipo : {}\nPower = {}\n'.format(self.especie, self.tipo, self.power)

    def attack(self, pokemon):
        attack = 10
        print("{}\nAtacou .....{} ".format(self, pokemon))
        pokemon.power = pokemon.power - attack
        print(f'sua força de ataque foi ... {attack}')
        print('Seu força caiu para', pokemon.power)


class PokemonEletrico(Pokemon):
    tipo = 'Eletrico'

    def attack(self, pokemon):
        attack = 20
        self.level += 1
        print('{} seu Level subiu, novo Level {}'.format(self.name, self.level))
        print(self)
        pokemon.power = pokemon.power - attack
        print('{} Lançou um Raio no {}'.format(self.name, pokemon))

    def choque220(self, pokemon):
        xoq_attack = 50
        pokemon.power -= xoq_attack
        print("{} Deu choque 220 , fritou {}".format(self.name, pokemon))
        print('{} danificou seu inimigo {}'.format(self.name, xoq_attack))


class PokemonFogo(Pokemon):
    tipo = 'Fogo'
    
    def attack(self, pokemon):
        attack = 20
        self.level += 1
        print('{} seu Level subiu, novo Level {}'.format(self.name, self.level))
        print(self)
        pokemon.power = pokemon.power - attack
        print('{} Lançou Uma bola de FOGO => no {}'.format(self.name, pokemon))


class PokemonAgua(Pokemon):
    tipo = 'Agua'
    
    def attack(self, pokemon):
        attack = 20
        self.level += 1
        print('{} seu Level subiu, novo Level {}'.format(self.name, self.level))
        print(self)
        pokemon.power = pokemon.power - attack
        print('{} Lançou Um Jato de ÁGUA => no {}'.format(self.name, pokemon))


p1 = Pokemon('Chamamix', name='ZOARK')
p2 = Pokemon('Pikachu')
print(p1)
p1.attack(p2)
print("pokemon eletrico criando")
print("**********************************")
print("")
p3 = PokemonEletrico("pikachu", name="JAIR")
print(p3)
print("")
print("**********************************")
print("")
p3.attack(p1)
print(p1)
print("")
print("**********************************")
print("")
p3.choque220(p1)

p4 = PokemonAgua('Torneirinha', name='TORNERA')
print(p4)

