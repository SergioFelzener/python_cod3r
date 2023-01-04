#!/usr/bin/python
# Conceitos   Notas
# A           De 10,0 a 9,1
# A-          De 9,0 a 8,1
# B           De 8,0 a 7,1
# B-          De 7,0 a 6,1
# C           De 6,0 a 5,1
# C-          De 5,0 a 4,1
# D           De 4,0 a 3,1
# D-          De 3,0 a 2,1
# E           De 2,0 a 1,1
# E-          De 1,0 a 0,1

# *Para notas maiores que 10 e menos que zero será impresso "Nota Invalida"

def calcula_conceito(nota):
    if nota > 10 or nota <= 0:
        print("Nota Invalida, utilize valores entre 10 à 0") 
    elif nota <= 10 and nota >= 9.1:
        conceito = "A"
        print(f"Seu conceito é {conceito}")
    elif nota <= 9.0 and nota >= 8.1:
        conceito = "A-"
        print(f"Seu conceito é {conceito}")
    elif nota <= 8.0 and nota >= 7.1:
        conceito = "B"
        print(f"Seu conceito é {conceito}")
    elif nota <= 7.0 and nota >= 6.1:
        conceito = "B-"
        print(f"Seu conceito é {conceito}")
    elif nota <= 6.0 and nota >= 5.1:
        conceito = "C"
        print(f"Seu conceito é {conceito}")
    elif nota <= 5.0 and nota >= 4.1:
        conceito = "C-"
        print(f"Seu conceito é {conceito}")
    elif nota <= 4.0 and nota >= 3.1:
        conceito = "D"
        print(f"Seu conceito é {conceito}")
    elif nota <= 3.0 and nota >= 2.1:
        conceito = "D-"
        print(f"Seu conceito é {conceito}")
    elif nota <= 2.0  and nota >= 1.1:
        conceito = "E"
        print(f"Seu conceito é {conceito}")
    elif nota <= 1.0 and nota >= 0.1:
        conceito = "E-"
        print(f"Seu conceito é {conceito}")

nota_input = input("Digite a Nota do Aluno para saber o conceito :")
nota = float(nota_input)
calcula_conceito(nota)


