from string import Template

nome, idade = 'Ana', 30.9873

print('Nome: %s\nIdade: %d' %(nome, idade))
print('Nome: %s\nIdade: %.1f' %(nome, idade))
print('Nome: %s\nIdade: %.2f' %(nome, idade))
print('Nome: %s\nIdade: %d %r %r'  %(nome, idade, True, False))

print('Nome {0} Idade {1}'.format(nome, idade))
print(f'Nome {nome} Idade {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))

