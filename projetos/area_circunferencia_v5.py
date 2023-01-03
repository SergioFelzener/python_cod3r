#!/usr/bin/python
from math import pi

# print(dir())
# print('π =', pi)

if __name__ == '__main__':
    try:
        raio = input('Informe o Raio : ')
        print("Área da circunferência :", pi * float(raio) ** 2)
    except Exception as error:
        print('Erro no programa', error)

