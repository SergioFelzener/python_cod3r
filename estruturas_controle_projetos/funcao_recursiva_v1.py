#!/usr/bin/python

# função recursiva que chama ela mesma
def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(imprimir(maximo, atual + 1))


imprimir(990, 1)
