#!/usr/bin/python

# fecha o recurso quando o bloco for finalizado (no caso já fecha o arquivo)
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        # print('Nome : {} Idade : {}'.format(*registro.split(',')))
        print('Nome : {} Idade : {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print("arquivo já foi fechado")
