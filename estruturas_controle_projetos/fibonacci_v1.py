#!/usr/bin/python
# sequencia [0, 1] = 1  / [1, 1] = 2 / [1, 2] = 3 / [2, 3] = 5 / [3, 5] = 8 / [5, 8] = 13 / [8, 13] = 21 / [13, 21] = 34 / [21, 34] = 55 / .....
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo_numero = penultimo + ultimo
        print(proximo_numero, end=',')
        penultimo = ultimo
        ultimo = proximo_numero
        if ultimo == 6765:
            break


if __name__ == '__main__':
    fibonacci()
