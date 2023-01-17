def executar(funcao):
    if callable(funcao):
        funcao()
    
def bom_dia():
    print("Bom Dia")

def boa_tarde():
    print("Boa Tarde")

def boa_noite():
    print("Boa Noite")
    
if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(boa_noite)
    executar(1)
    