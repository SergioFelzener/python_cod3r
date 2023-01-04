# while True:
#     print('Vai demorar muito')

from random import randint

numero_informado = -1
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input("Informe o número secreto : "))

print("o Número secreto {} foi digitado ".format(numero_secreto))