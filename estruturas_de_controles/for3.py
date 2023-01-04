produto = {"nome": "canet xique", "preço": 14.99,
           "Importada": True, "estoque": 793}

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)
    
for key, value in produto.items():
    print(key, "=", value)
    
# chave e valor ficam disponíveis fora do for o ultimo antes de sair do laço

print(key, value, chave, valor)