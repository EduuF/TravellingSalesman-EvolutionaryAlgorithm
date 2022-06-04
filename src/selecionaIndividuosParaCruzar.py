import random


def selecionaIndividuosParaCruzar(individuosOrdenados):
    sorteio1 = random.randint(1, 100)

    individuoSorteado = 0

    if sorteio1 <= 30:
        individuoSorteado = individuosOrdenados[1]
    if 50 >= sorteio1 > 30:
        individuoSorteado = individuosOrdenados[2]
    if 65 >= sorteio1 > 50:
        individuoSorteado = individuosOrdenados[3]
    if 77 >= sorteio1 > 65:
        individuoSorteado = individuosOrdenados[4]
    if 88 >= sorteio1 > 77:
        individuoSorteado = individuosOrdenados[5]
    if 94 >= sorteio1 > 88:
        individuoSorteado = individuosOrdenados[6]
    if 98 >= sorteio1 > 94:
        individuoSorteado = individuosOrdenados[7]
    if 100 >= sorteio1 > 98:
        individuoSorteado = individuosOrdenados[8]

    return individuoSorteado




