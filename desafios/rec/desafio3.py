#!/usr/bin/python
import sys

def calc_pintura(area):
    qntd_tinta = area / 3
    qntd_latas = qntd_tinta / 18
    qntd_latas = int(qntd_latas) + 1
    total = qntd_latas * 80.00

    return (qntd_latas, total)

if __name__ == "__main__":
    area = float(sys.argv[1])
    qntd_latas, total = calc_pintura(area)

    print(f"Quantidade de latas necessárias: {qntd_latas}")
    print(f"Preço total das latas: R$_{total}")