import numpy as np

# local libs
from src.geraPermutacoes import gera_permutacoes
from src.calculaDistancia import calcula_distancia
from src.ordenaMelhoresIndividuos import ordenaMelhoresIndividuos
from src.cruzaIndividuos import cruzaIndividuos
from src.selecionaIndividuosParaCruzar import selecionaIndividuosParaCruzar


def caixeiro_viajante(distancias, QUANTIDADE_INDIVIDUOS, TAXA_DE_MUTACAO, NUMERO_DE_GERACOES):
    individuos = gera_permutacoes()
    distanciasPercorridas = calcula_distancia(individuos, distancias)

    melhoresDistanciaPorEpoca = []
    melhoresIndividuos = []

    for i in range(NUMERO_DE_GERACOES):
        individuosOrdenados = ordenaMelhoresIndividuos(individuos, distanciasPercorridas)

        individuoSelecionado = selecionaIndividuosParaCruzar(individuosOrdenados)

        individuoUm, individuoDois, individuoTres = cruzaIndividuos(individuosOrdenados[0],
                                                                    individuoSelecionado,
                                                                    TAXA_DE_MUTACAO)

        individuos = [individuosOrdenados[0], individuoDois, individuoTres]

        for j in range(QUANTIDADE_INDIVIDUOS - 3):
            novoIndividuo = individuosOrdenados[j+3]
            individuos.append(novoIndividuo)

        distanciasPercorridas = calcula_distancia(individuos, distancias)

        melhoresIndividuos.append(individuoUm)
        melhoresDistanciaPorEpoca.append(min(distanciasPercorridas))

    return [melhoresDistanciaPorEpoca, melhoresIndividuos]