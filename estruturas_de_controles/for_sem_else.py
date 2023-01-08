PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia é divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Possuí pelo menos uma palavra proibida', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado', texto)

