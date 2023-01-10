#!/usr/bin/python
# sequencia [0, 1] = 1  / [1, 1] = 2 / [1, 2] = 3 / [2, 3] = 5 / [3, 5] = 8 / [5, 8] = 13 / [8, 13] = 21 / [13, 21] = 34 / [21, 34] = 55 / .....
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado
               
        
        
if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
