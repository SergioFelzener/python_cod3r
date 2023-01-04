#!/usr/bin/python
from math import pi
import sys
import errno

# print(dir())
# print('π =', pi)


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    script = sys.argv[0][2:]
    print('É necessário informar raio do circulo')
    print(f'Sintaxe: {script} <raio>')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            help()
            sys.exit(errno.EPERM)
        elif not sys.argv[1].isnumeric():
            help()
            print('O Raio deve ser um valor numérico')
        else:
            raio = sys.argv[1]
            area = circulo(raio)
            print('Àrea do circulo :', area)
    except Exception as error:
        print('Necessário informar o valor do raio')
        print('')
        print('***********************************')
        print('ex. ./area_circunferencia_v8.py 10')
        print('***********************************')
        print('')
        print('Erro no programa', error)
        print('')
