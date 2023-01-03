#!/usr/bin/python
from math import pi

# print(dir())
# print('π =', pi)


def circulo(raio):
    print("Área da circunferência :", pi * float(raio) ** 2)


if __name__ == '__main__':
    try:
        raio = input('Informe o Raio : ')
        circulo(raio)
    except Exception as error:
        print('Erro no programa', error)
