#!/usr/bin/python3

from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir_tarefa(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluído)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

   # usando list comprehension
    [tarefa.concluir_tarefa() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f' - {tarefa}')


if __name__ == '__main__':
    main()
