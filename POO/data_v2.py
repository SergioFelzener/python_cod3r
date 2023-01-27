class Data:
    def __init__(self, dia=12, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # def to_str(self):
    #     return f'{self.dia}/{self.mes}/{self.ano}'

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

print('name : ', __name__)
if __name__ == '__main__':
    d1 = Data(5, 1, 2023)
    # d1.dia = 5
    # d1.ano = 2023
    # d1.mes = 1
    print(d1)
    # try:
    #     print(d1)
    # except Exception as error:
    #     print('Erro =>', error)

    d2 = Data(ano=2022)
    d2.dia = 10
    # d2.a = 2021
    # d2.m = 2
    print(d2)
    print(type(d2))
    
    d3 = Data()
    print(d3)
