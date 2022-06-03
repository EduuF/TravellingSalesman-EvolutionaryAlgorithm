import numpy as np

# local libs
from src.geraPermutacoes import gera_permutacoes
from src.calculaDistancia import calcula_distancia
from src.ordenaMelhoresIndividuos import ordenaMelhoresIndividuos
from src.cruzaIndividuos import cruzaIndividuos

def caixeiro_viajante(distancias, QUANTIDADE_INDIVIDUOS, TAXA_DE_MUTACAO):

  individuos = gera_permutacoes()
  distanciasPercorridas = calcula_distancia(individuos, distancias)

  melhoresDistanciaPorEpoca = []
  melhoresIndividuos = []

  for i in range(100000):
    individuosOrdenados = ordenaMelhoresIndividuos(individuos, distanciasPercorridas)
    individuoUm, individuoDois, individuoTres = cruzaIndividuos(individuosOrdenados[0], individuosOrdenados[1], TAXA_DE_MUTACAO)

    individuos = [individuoUm, individuoDois, individuoTres]

    for j in range(QUANTIDADE_INDIVIDUOS - 3):
      novoIndividuo = [0,1,2,3,4]
      np.random.shuffle(novoIndividuo)
      individuos.append(novoIndividuo)

    distanciasPercorridas = calcula_distancia(individuos, distancias)

    melhoresIndividuos.append(individuoUm)
    melhoresDistanciaPorEpoca.append(min(distanciasPercorridas))


  return([melhoresDistanciaPorEpoca, melhoresIndividuos])
