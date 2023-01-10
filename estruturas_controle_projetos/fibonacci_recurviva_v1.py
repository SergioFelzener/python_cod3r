#!/usr/bin/python3

def fibonnaci(quantidade, sequencia=(0,1)):
    #Importante : Condição de Parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    # Listar os 20 primeiro números da sequencia de fibonacci
    for fib in fibonnaci(20):
        print(fib)


    