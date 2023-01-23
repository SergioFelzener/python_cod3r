#!/usr/bin/python3

def fibonacci(sequencia=[0,1]):
    #uso de mutaveis com o valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    try:    
        assert restart == [0, 1, 1]
    except Exception as error:
        print('error : ', error)