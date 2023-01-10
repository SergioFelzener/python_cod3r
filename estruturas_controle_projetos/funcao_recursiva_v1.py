#!/usr/bin/python
# sequencia [0, 1] = 1  / [1, 1] = 2 / [1, 2] = 3 / [2, 3] = 5 / [3, 5] = 8 / [5, 8] = 13 / [8, 13] = 21 / [13, 21] = 34 / [21, 34] = 55 / .....
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(imprimir(maximo, atual + 1))

imprimir(990, 1)