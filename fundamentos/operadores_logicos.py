print(True or False)

print(7 != 3 and 2 > 3)

# tabela verdade
# operador and
print("tabela verdade 'AND'  V e F")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# operador or
print("tabela verdade 'OR'  V e F")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("tabela verdade 'XOR'  V e F")
# operador xor (ou exclusivo != usa diferente)
# print(True != True)
# print(True != False)
# print(False != True)
# print(False != False)
print("diferente funciona como 'XOR' != ")
# operador negação "not"
print("Operadores de negação")
print(not True)
print(not False)

print(not 0)
print(not 1)
print(not not -1)
print(not not True)
# cuidado
print("**** cuidado *****")
print(True & True)
print(True & False)
print(True | True)
print(True ^ True)

# 3 = 11 (binário)
print("and bit-a-bit")
# 3 = 11
# 2 = 10
print(3 & 2)

print("or bit-a-bit")
# 3 = 11
# 2 = 10
print(3 | 2)

print("xor bit-a-bit")
# 3 = 11
# 2 = 10
print(3 ^ 2)


# um pouco de realidade
saldo = 1000
salario = 4000
despesas = 3967

meta = saldo > 0 and salario - despesas >= 0.20 * salario
print(meta)
