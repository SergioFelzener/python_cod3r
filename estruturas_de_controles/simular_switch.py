def get_dias_semana(dia):
    dias = {1: "domingo", 2: "segunda", 3: "terça",
            4: "quarta", 5: "quinta", 6: "sexta", 7: "sábado"}
    return dias.get(dia, '** Dia Inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f"{dia}: {get_dias_semana(dia)}")
