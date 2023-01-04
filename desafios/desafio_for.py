# Funcao sortear_dado numeros entre 1 a 6
# for com range de 1 a 6
# se for impar continue 
# se o numero for par e for igual ao valor sorteado 
# pela funcao dado imprimir "acertou" e depois chamar o break
# se não acertar chamar o else ... print("não acertou")
from random import randint

def sortear_dado():
    numero = randint(1,6)
    # print("numero dentro da função =", numero)
    return numero

if __name__ == "__main__":
    numero_sorteado = sortear_dado()
    # print("numero dentro do Main =", numero_sorteado)

    for i in range(1,7):
        # print("número sorteado dentro do laço =", numero_sorteado)
        if numero_sorteado % 2 == 1:
            continue
        
        if numero_sorteado == i:
            print("ACERTOU !!! {}".format(numero_sorteado))
            break
            # print(numero_sorteado)
    else:
        print("Não Acertou o número {} que foi sorteado".format(numero_sorteado))
    

