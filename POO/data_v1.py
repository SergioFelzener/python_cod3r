class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    def __str__(self):
        return f'{self.d}/{self.m}/{self.a}'


d1 = Data()
d1.dia = 5
d1.ano = 2023
d1.mes = 1
print(d1.to_str())

d2 = Data()
d2.d = 10
d2.a = 2021
d2.m = 2
print(d2)
print(type(d2))
