# Tupla não pode ser modificada, não pode adicionar novos elementos

tupla = ()
print(type(tupla))
# print(dir(tupla))
# print(help(tupla))

tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))
print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'branco', 'azul')

print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores[:-1])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))

