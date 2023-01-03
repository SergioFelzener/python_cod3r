#!/usr/bin/python
from math import pi

# print(dir())
# print('π =', pi)


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    try:
        raio = input('Informe o Raio : ')
        area = circulo(raio)
        print('Àrea do circulo : ', area)
    except Exception as error:
        print('Erro no programa', error)
