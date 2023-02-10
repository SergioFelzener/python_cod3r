#!/usr/bin/python

class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
    
if __name__ == '__main__':
    jose = Humano('Jose')
    gronk = Humano('Gronk').das_cavernas()
    # print(gronk.das_cavernas() is None)
    
    print(f'Humano.epecie : {Humano.especie}')
    print(f'jose.epecie : {jose.especie}')
    print(f'gronk.epecie : {gronk.especie}')
    
    
    
    