def get_dias_final_de_semana(dia):
    dias = {1: "domingo", 2: "segunda", 3: "terça",
            4: "quarta", 5: "quinta", 6: "sexta", 7: "sábado"}
    return dias.get(dia, '** Dia de Semama **')


if __name__ == '__main__':
    for dia in range(1, 8):
        # if dia != 2 and dia != 3 and dia !=4 and dia != 5 and dia !=6:
        print(f"{dia}: {get_dias_final_de_semana(dia)}")
