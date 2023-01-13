#!/usr/bin/python
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        # print('Nome : {} Idade : {}'.format(*registro.split(',')))
        print('Nome : {} Idade : {}'.format(registro.strip().split(',')))
except Exception as error:
        print("Erro na execução", error)
        pass
finally:
    print("fechando arquivo")
    arquivo.close()
    print("arquivo Fechado")
    
if arquivo.closed:
    print("arquivo já foi fechado")
