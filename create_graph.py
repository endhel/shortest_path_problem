from random import randint, choice


def create_graph(num_vertices, num_edges, min_weight, max_weight):
    graph = []

    for i in range(num_vertices):
        graph.append([])
    for j in range(num_edges):
        v = randint(0, num_vertices - 1)

        if len(graph[v]) == 0:
            interval = []
            for i in range(num_vertices):
                if i != v:
                    interval.append(i)
            adjacent = [choice(interval), ]
            weight = [randint(min_weight, max_weight), ]
            graph[v].append(adjacent)
            graph[v].append(weight)
        else:
            interval = []
            for k in range(num_vertices):
                if k != v and k not in graph[v][0]:
                    interval.append(k)
            if len(interval) > 0:
                graph[v][0].append(choice(interval))
                graph[v][1].append(randint(min_weight, max_weight))

    for i in range(len(graph)):
        if len(graph[i]) > 0:
            graph[i][0] = tuple(graph[i][0])
            graph[i][1] = tuple(graph[i][1])

    return graph
