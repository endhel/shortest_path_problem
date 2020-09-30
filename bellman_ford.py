def bellman_ford(g, origin):
    distance = []
    predecessor = []

    for i in range(len(g)):
        distance.append(float('inf'))
        predecessor.append(None)
    distance[origin] = 0
    vertices = [i for i in range(len(g))]

    for _ in range(len(vertices)):
        change = False
        for i in range(len(vertices)):
            index = 0
            if len(g[i]) > 0:
                for j in g[i][0]:
                    if distance[j] > distance[i] + g[i][1][index]:
                        distance[j] = distance[i] + g[i][1][index]
                        predecessor[j] = i
                        change = True
                    index += 1
        if not change:
            break

    return distance, predecessor
