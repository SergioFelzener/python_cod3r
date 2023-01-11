def fibonacci():
    pergunta = int(input("Quantos nuúmeros de fibonacci deseja ver? "))
    i = 0
    var1 = 0
    var2 = 1
    varSoma = 1
    
    while i < pergunta:
        print("|")
        print(var1)
        varSoma = var1 + var2
        var1 = var2
        var2 = varSoma
        i+=1
    return

fibonacci()
        