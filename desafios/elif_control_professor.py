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

def nota_conceito(valor):
    nota = float(valor)
    
    if nota > 10:
        return 'Nota invalida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Invalida'
    
    
if __name__ == '__main__':
    nota_input = input('Digite a nota : ')
    conceito = nota_conceito(nota_input)
    print(conceito)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    