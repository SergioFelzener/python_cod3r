def faixa_etaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade"
    elif idade in range(18, 64):
        return "Adulto"
    elif idade in range(65, 100):
        return "Idoso Preferencial"
    elif idade > 100:
        return "Centenario"
    else:
        return "idade invalida"


if __name__ == '__main__':
    for idade in (17, 35, 87, 113, 0, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
