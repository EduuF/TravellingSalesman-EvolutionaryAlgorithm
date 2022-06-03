def calcula_distancia(individuos, distancias):

  distanciasPercorridas = []

  for individuo in individuos: # [0,2,4,1,3]
    distanciaCaminhada = 0

    for cidade in range(4): # 0, 1, 2, 3
      distanciaCaminhada += distancias[individuo[cidade]][individuo[cidade+1]]

      # Da ultima cidade de volta à primeira
      if(cidade == (len(individuo)-2)):
        distanciaCaminhada += distancias[individuo[cidade+1]][individuo[0]]

    distanciasPercorridas.append(distanciaCaminhada)

  return distanciasPercorridas