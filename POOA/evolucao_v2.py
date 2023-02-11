#!/usr/bin/python

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

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
    gronk = Neanderthal('Gronk')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido ? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal é evoluido ? {Neanderthal.is_evoluido()}')
    print(f'Jose é evoluido ? {jose.is_evoluido()}')
    print(f'Gronk é evoluido ? {gronk.is_evoluido()}')
