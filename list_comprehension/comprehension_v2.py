# [expressão for item in list if conditional ]

dobro_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_dos_pares)


# versao normal sem list comprehension
dobros_dos_pares = [] 

for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print("dobros dos pares normal", dobros_dos_pares)