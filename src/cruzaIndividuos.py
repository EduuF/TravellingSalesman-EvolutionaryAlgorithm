import random

# local libs
from src.mutaIndividuo import mutaIndividuo

def cruzaIndividuos(primeiroIndividuo, segundoIndividuo, TAXA_DE_MUTACAO):
    pontoDeCorte = random.randint(int(len(primeiroIndividuo) / 2),
                                  len(primeiroIndividuo) - int(len(primeiroIndividuo) / 4))

    filhoUm = primeiroIndividuo[:pontoDeCorte] + segundoIndividuo[pontoDeCorte:]
    filhoDois = segundoIndividuo[:pontoDeCorte] + primeiroIndividuo[pontoDeCorte:]

    for i in range(len(primeiroIndividuo) - pontoDeCorte):
        if filhoUm[pontoDeCorte + i] in filhoUm[:pontoDeCorte + i]:

            break_flag = False
            for j in range(len(primeiroIndividuo)):

                if (j not in filhoUm and break_flag == False):
                    filhoUm[pontoDeCorte + i] = j
                    break_flag = True

    for i in range(len(primeiroIndividuo) - pontoDeCorte):
        if filhoDois[pontoDeCorte + i] in filhoDois[:pontoDeCorte + i]:

            break_flag = False
            for j in range(len(primeiroIndividuo)):

                if j not in filhoDois and break_flag == False:
                    filhoDois[pontoDeCorte + i] = j
                    break_flag = True

    # Muta filho 1
    chanceDeMutar = random.randint(1, 100)
    if (chanceDeMutar <= TAXA_DE_MUTACAO):
        filhoUm = mutaIndividuo(filhoUm)

    # Muta filho 2
    chanceDeMutar = random.randint(1, 100)
    if (chanceDeMutar <= TAXA_DE_MUTACAO):
        filhoDois = mutaIndividuo(filhoDois)

    return primeiroIndividuo, filhoUm, filhoDois