def contar_leds(numero):
    resultado = 0
    leds_por_numero = {
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "0": 6
    }

    for caractere in numero:
        resultado += leds_por_numero.get(caractere, 0)
    return resultado

if __name__ == "__main__":
    numero = "1234567890"
    leds_total = contar_leds(numero)
    print("Quantidade de LEDs necessários: ", leds_total)