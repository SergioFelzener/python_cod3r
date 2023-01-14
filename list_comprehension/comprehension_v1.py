# [expressão for item in list if conditional ]

dobros = [i * 2 for i in range(10)]
print(dobros)

# versao normal sem list comprehension
dobros = [] 

for i in range(10):
    dobros.append(i * 2)
print("dobros normal", dobros)
