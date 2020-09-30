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
        if u == -1:
            break
        adjacency = g[u]
        vertices.remove(u)
        index = 0

        if len(adjacency) > 0:
            for v in adjacency[0]:
                if distance[v] > distance[u] + adjacency[1][index]:
                    distance[v] = distance[u] + adjacency[1][index]
                    predecessor[v] = u
                index += 1

    return distance, predecessor
