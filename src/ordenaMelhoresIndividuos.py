def ordenaMelhoresIndividuos(individuos, distanciasPercorridas):
    permutacoesOrdenadas = []

    # Faz a cópia das listas
    _distanciasPercorridas, _individuos = distanciasPercorridas.copy(), individuos.copy()

    for i in range(len(individuos)):
        # Calcula menor distancia, index e melhor individuo
        menorDistancia = min(_distanciasPercorridas)
        indexMenorDistancia = _distanciasPercorridas.index(menorDistancia)
        melhorIndividuo = _individuos[indexMenorDistancia]

        # Adiciona a melhor à lista
        permutacoesOrdenadas.append(melhorIndividuo)

        # Deleta a melhor da lista provisória
        del _individuos[indexMenorDistancia]
        del _distanciasPercorridas[indexMenorDistancia]

    return permutacoesOrdenadas