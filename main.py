from confing import QUANTIDADE_INDIVIDUOS, TAXA_DE_MUTACAO, NUMERO_DE_GERACOES, distancias
from src.caixeiroViajante import caixeiro_viajante

from collections import Counter

resultado = caixeiro_viajante(distancias, QUANTIDADE_INDIVIDUOS, TAXA_DE_MUTACAO, NUMERO_DE_GERACOES)

print(Counter(resultado[0]))