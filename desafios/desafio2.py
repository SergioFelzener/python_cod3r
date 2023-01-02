# desafio operadores lógicos
"""
pessoa tem 2 trabalhos para executar um terça outro quinta
os dois trabalhos dando certo compra uma tv 50 e toma sorvete para comemorar
um dando certo tv 32 + sorvete 
nenhum dando certo fica em casa sem sorvete e televisão
"""

trabalho_terca = True
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # xor
fica_em_casa = not sorvete

print("TV_50 = {}\nTV_32 = {}\nSorvete = {}\nFica em Casa = {}\n".format(
    tv_50, tv_32, sorvete, fica_em_casa))
