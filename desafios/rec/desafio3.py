#!/usr/bin/python
import sys

def calc_pintura(area):
    quantidade_tinta = area / 3
    quantidade_latas = quantidade_tinta / 18
    quantidade_latas = int(quantidade_latas) + 1
    preco_total = quantidade_latas * 80.00

    return (qntd_latas, total)

if __name__ == "__main__":
    area = float(sys.argv[1])
    qntd_latas, total = calc_pintura(area)

    print(f"Quantidade de latas necessárias: {qntd_latas}")
    print(f"Preço total das latas: R$_{total}")