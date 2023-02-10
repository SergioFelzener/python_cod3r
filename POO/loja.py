#!/usr/bin/python3
from datetime import datetime
try:
    from loja import Cliente, Vendedor, Compra
except Exception as error:
    print('Error ===> ', error)

def main():
    cliente = Cliente("Maria Lima", 44)
    vendedor = Vendedor("Pedro Garrido", 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 4), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtd_compras = len(cliente.compras)
    print(f'Total : {valor_total} em {qtd_compras} compras')
    print(f'Última Compra : {cliente.get_data_ultima_compra()}')


if __name__ == "__main__":
    try: 
        main()
    except Exception as error:
        print('Error MAIN() --> ', error)