#!/usr/bin/python

# fecha o recurso quando o bloco for finalizado (no caso já fecha o arquivo)
with open('pessoas.csv', ) as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            # print('Nome : {} Idade : {}'.format(*registro.split(',')))
            pessoa = registro.strip().split(',')
            print('Nome : {} Idade : {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print("arquivo já foi fechado")
    
if saida.closed:
    print("arquivo de saída já foi fechado")
