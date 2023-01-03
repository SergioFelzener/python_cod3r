# conjunto não aceita repetição nao é indexado 

a = {1, 3, 6}
print(type(a))
a = set('cod3r')
print(a)
print('3' in a, 4 not in a)
print({1, 2, 3} == {2, 3, 1, 3})

#operações
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)
print(c2 <= c1)
print(c1 >= c2)
print({1, 2, 3} - {3})
print(c1 - c2)
print(c1)
c1 -= {2}
print(c1)

