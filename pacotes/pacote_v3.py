# resolvendo conflito de modulos com mesmo nome

from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub # resolvendo conflito com alias "as" <alias>

print('Soma', modulo1.soma(2, 4))
print('Subtração ', modulo1_sub.sub(2, 4))
