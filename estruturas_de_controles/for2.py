palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=',')
print('\nfim')


aprovados = ["Rafaela", "Pedro", "Renato", "Maria"]
for nome in aprovados:
    print(nome)
    
    
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)
    
dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta"]    
for dia in dias_semana:
    print(f"Hoje é {dia}-feira")
    
    
for letra in set('Muito Legal'):
    print(letra)
    
for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
    print(numero)
    
print(type({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
print(type(set("muito Legal")))