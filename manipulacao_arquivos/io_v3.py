#!/usr/bin/python

arquivo = open('pessoas.csv')
for registro in arquivo:
    # print('Nome : {} Idade : {}'.format(*registro.split(',')))
    print('Nome : {} Idade : {}'.format(*registro.strip().split(',')))
arquivo.close()
