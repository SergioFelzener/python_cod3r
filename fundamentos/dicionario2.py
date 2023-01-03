pessoa = {'nome': 'Prof(a) Alberto', 'idade': 45,
          'cursos': ['React', 'Python']}
print(pessoa)
pessoa['idade'] = 48
print(pessoa)
pessoa['cursos'].append('Angular')
print(pessoa)
print(pessoa.pop('idade'))
pessoa.update({'idade': 48, 'sexo': 'Masculino'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
