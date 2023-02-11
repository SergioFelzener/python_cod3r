#!/usr/bin/python

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade
        return self

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo estático não recebe parametro
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Austalopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]  # pegando neaderthalensis


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]  # pegando Saiepns


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    try:
        jose.idade = -40
    except Exception as error:
        print('Error >> ' , error)
    #    jose._idade(40)
    print(f'Nome : {jose.nome}, Idade({jose.idade})')