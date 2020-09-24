def dijkstra(g, origin):
    distance = []
    predecessor = []

    for i in range(len(g)):
        distance.append(float('inf'))
        predecessor.append(None)
    distance[origin] = 0
    vertices = [i for i in range(len(g))]

    while len(vertices) != 0:
        minimum = float('inf')
        u = -1
        for i in vertices:
            if distance[i] < minimum:
                minimum = distance[i]
                u = i
        adjacency = g[u]
        vertices.remove(u)
        index = 0

        for v in adjacency[0]:
            if distance[v] > distance[u] + adjacency[1][index]:
                distance[v] = distance[u] + adjacency[1][index]
                predecessor[v] = u
            index += 1

    print(distance)
    print(predecessor)


graph = [[(1, 2, 3), (3, 1, 1)],
         [(2, 4), (4, 1)],
         [(0, 1, 3, 4), (1, 4, 5, 5)],
         [(0,), (1,)],
         [(0, 2, 3), (4, 5, 2)]]

dijkstra(graph, 2)
