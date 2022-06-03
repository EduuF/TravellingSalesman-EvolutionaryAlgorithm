import random

def mutaIndividuo(individuo):
  posicaoUm = random.randint(0,4)
  posicaoDois = random.randint(0,4)

  # Evita que as duas posicoes sejam a mesma
  while(posicaoDois == posicaoUm):
    posicaoDois = random.randint(0,4)

  # Troca posicoes
  individuo[posicaoUm], individuo[posicaoDois] = individuo[posicaoDois], individuo[posicaoUm]
  return individuo