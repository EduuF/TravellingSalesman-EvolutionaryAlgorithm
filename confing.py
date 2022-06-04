

QUANTIDADE_INDIVIDUOS = 10
TAXA_DE_MUTACAO = 3
NUMERO_DE_GERACOES = 100000

''' Random Dataset
distancias = [
                [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
                [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
                [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
                [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
                [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
                [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
                [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
                [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
                [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
                [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
                [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
                [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
                [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0]
             ] 

'''

cidades = {'Belo Horizonte': 0,
           'São Paulo': 1,
           'Rio de Janeiro': 2,
           'Porto Alegre': 3,
           'Salvador': 4,
           'Recife': 5,
           'Brasilia': 6,
           'Goiania': 7,
           'Cuiabá': 8}

distancias = [
    [0, 585, 442, 1720, 1400, 2094, 734, 887, 1570],
    [585, 0, 435, 1132, 1962, 2638, 1005, 889, 1525],
    [442, 435, 0, 1569, 1632, 2384, 1166, 1300, 1926],
    [1720, 1132, 1569, 0, 3104, 3781, 2122, 2015, 2125],
    [1400, 1962, 1632, 3104, 0, 823, 1444, 1646, 2504],
    [2094, 2638, 2384, 3781, 823, 0, 2120, 2322, 3180],
    [734, 1005, 1166, 2122, 1444, 2120, 0, 209, 1070],
    [887, 899, 1300, 2015, 1646, 2322, 209, 0, 888],
    [1570, 1528, 1926, 2125, 2304, 3180, 1070, 888, 0]
]