def validate ():

    d = int(input("Informe o dia: "))
    m = int(input("Informe o mês: "))
    y = int(input("Informe o ano: "))


    if d > 31 or d < 1:
        print ("dia inválido")
    elif m > 12 or m < 1:
        return print ("Mês inválido")
    elif y > 2026:
        return print("Ano inválido")

    return verify(y)

def verify (y):
    if (y % 4) == 0:
        return print("Bissexto")
    elif (y % 4) != 0:
        return print("Não bissexto")


validate()