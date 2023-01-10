#!/usr/bin/python
# sequencia [0, 1] = 1  / [1, 1] = 2 / [1, 2] = 3 / [2, 3] = 5 / [3, 5] = 8 / [5, 8] = 13 / [8, 13] = 21 / [13, 21] = 34 / [21, 34] = 55 / .....
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(quantidade - 2):
    # for i in range(quantidade - 2):
    # for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado
               
        
        
if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
