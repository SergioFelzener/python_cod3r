from decimal import Decimal, getcontext

print(1.1 + 2.2)  # resultado em 3.3000000000000003

print(Decimal(1) / Decimal(7))  # resultado 0.1428571428571428571428571429
getcontext().prec = 4  # mudando precisao de casa decimal
print(Decimal(1) / Decimal(7))  # resultado 0.1429

print(Decimal.max(Decimal(1), Decimal(7)))  # printa maior decimal entre eles

print("o que está disponível dentro de Decimal")
print(" \n*************** dir(Decimal) *****************\n")
print(dir(Decimal))

print(" \n*************** dir(Decimal) *****************\n")

print(Decimal(1.1) + Decimal(2.2))
print(" \n******** Verificação de disponibilidade global **********\n")
print(" \n*************** dir() *****************\n")
print(dir())
print("fim")
