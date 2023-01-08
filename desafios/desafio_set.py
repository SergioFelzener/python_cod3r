PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia é divertida'
]

print(type(PALAVRAS_PROIBIDAS))
print(dir(set))

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto contém palavras proibidas : ', intersecao)
    else:
        print('Texto Autorizado : ', texto)
    