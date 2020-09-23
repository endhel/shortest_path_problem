def dijkstra(g, origin):
    dist = []
    pred = []

    for i in range(len(g)):
        dist.append(float('inf'))
        pred.append(None)
    dist[origin] = 0
    Q = g


graph = [[(1, 2), (2, 6)],
         [(2, 5), (4, 3)],
         [(1, 5), (3, 4)],
         [(0, 2), (4, 7)],
         [(0, 1), (3, 7)],
         []]

dijkstra(graph, 0)