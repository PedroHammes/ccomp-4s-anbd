def validate (d, m, y):
    if d > 31 or d < 1:
        print ("dia inválido")
    elif m > 12 or m < 1:
        return print ("Mês inválido")
    elif y > 2026:
        return print("Ano inválido")


    if (y % 4) == 0:
        return print("Bissexto")
    elif (y % 4) != 0:
        return print("Não bissexto")


validate(20, 12, 2022)