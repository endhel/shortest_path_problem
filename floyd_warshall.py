def floyd_warshall(g):
    distance = []
    predecessor = []
    for i in range(len(g)):
        predecessor.append([None for _ in range(len(g))])
        distance.append([float('inf') for _ in range(len(g))])
    for i in range(len(g)):
        for j in range(len(g)):
            if i == j:
                distance[i][j] = 0
            elif len(g[i]) > 0:
                if j in g[i][0]:
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

    return distance, predecessor
