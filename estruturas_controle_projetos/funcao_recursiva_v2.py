#!/usr/bin/python
# sequencia [0, 1] = 1  / [1, 1] = 2 / [1, 2] = 3 / [2, 3] = 5 / [3, 5] = 8 / [5, 8] = 13 / [8, 13] = 21 / [13, 21] = 34 / [21, 34] = 55 / .....
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

# função recursiva que chama a si própria

def imprimir(maximo, atual):
    # condição de parada
    if atual < maximo:
        print(atual)
        imprimir(imprimir(maximo, atual + 1))

imprimir(1000, 1)