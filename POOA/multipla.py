#!/usr/bin/python

class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('Fazer Teia', 'Andar pelas paredes')

class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'Atirar teias entre predios')

if __name__ == '__main__':
    
    john = Homem()
    print(f'John capacidades : {john.capacidades}')
    arack = Aranha()
    print(f'Arack capacidades : {arack.capacidades}')
    peter = HomemAranha()
    print(f'SupeHeroi capacidades : {peter.capacidades}')
    