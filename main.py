from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall
from create_graph import create_graph
import rec_path
from time import time


print('Grafo:')
graph = create_graph(4, 8, 1, 10)
for i in range(len(graph)):
    print(graph[i])
print()

option = int(input("Algoritmo: \n\t1 Dijkstra\n\t2 Bellman-Ford\n\t3 Floyd-Warshall\n"))
origin = int(input("Origem: "))
destiny = int(input("Destino: "))

print()
print('Processando...')
print()

inicio = time()
if option == 1:
    dist, pred = dijkstra(graph, origin)
    print('Vetor de distâncias: ', dist)
    print('Vetor de predecessores: ', pred)
    print('Caminho: ', rec_path.rec_path(pred, origin, destiny))
    print(f'Custo do Caminho: {dist[destiny]}')
    fim = time()
    print(f'Tempo: {fim - inicio}')
if option == 2:
    dist, pred = bellman_ford(graph, origin)
    print('Vetor de distâncias: ', dist)
    print('Vetor de predecessores: ', pred)
    print('Caminho: ', rec_path.rec_path(pred, origin, destiny))
    print(f'Custo do Caminho: {dist[destiny]}')
    fim = time()
    print(f'Tempo: {fim - inicio}')
if option == 3:
    dist, pred = floyd_warshall(graph)
    print('Matriz de distâncias:')
    for i in range(len(dist)):
        print(i, ' - ', end="")
        for j in range(len(dist)):
            print(dist[i][j], '', end="")
        print()
    print('\nMatriz de predecessores:')
    for i in range(len(pred)):
        print(i, ' - ', end="")
        for j in range(len(dist)):
            print(pred[i][j], '', end="")
        print()
    print('\nCaminho: ', rec_path.rec_path_floyd(pred, origin, destiny))
    print(f'Custo do Caminho: {dist[origin][destiny]}')
    fim = time()
    print(f'Tempo: {fim - inicio}')
