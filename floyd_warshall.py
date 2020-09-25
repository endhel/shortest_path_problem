import numpy as np


def floyd_warshall(g):
    distance = np.zeros((len(g), len(g)))
    predecessor = []
    for i in range(len(g)):
        predecessor.append([None] * len(g))

    for i in range(len(g)):
        for j in range(len(g)):
            if i == j:
                distance[i][j] = 0
            elif j in g[i][0]:
                index = list(g[i][0]).index(j)
                distance[i][j] = g[i][1][index]
                predecessor[i][j] = i
            else:
                distance[i][j] = float('inf')
                predecessor[i][j] = None

    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    predecessor[i][j] = predecessor[k][j]

    print(distance)
    print(predecessor)


graph = [[(1, 2), (6, 2)],
         [(0, 2, 3), (3, 7, 5)],
         [(1, 3), (2, 1)],
         [(2,), (4,)]]

floyd_warshall(graph)
