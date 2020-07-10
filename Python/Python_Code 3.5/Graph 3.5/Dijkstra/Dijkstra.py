I = float('inf')


def dijkstra(graph, n):
    closedge = [0] * n
    vertex = []
    distance = []
    flag = [False] * n
    flag[0] = True
    k = 0
    vertex.append(k)
    distance.append(0)
    for i in range(n):
        closedge[i] = graph[k][i]

    for j in range(n - 1):
        mini = I
        for i in range(n):
            if closedge[i] < mini and not flag[i]:
                mini = closedge[i]
                k = i
        if k == 0:  # 不连通
            return
        flag[k] = True
        vertex.append(k)
        distance.append(closedge[k])
        for i in range(n):
            if closedge[i] > closedge[k] + graph[k][i]:
                closedge[i] = closedge[k] + graph[k][i]
    return closedge, vertex, distance


if __name__ == '__main__':
    n = 6
    graph = [
        [0, 6, 3, I, I, I],
        [6, 0, 2, 5, I, I],
        [3, 2, 0, 3, 4, I],
        [I, 5, 3, 0, 2, 3],
        [I, I, 4, 2, 0, 5],
        [I, I, I, 3, 5, 0],
    ]
    closedge, vertex, distance = dijkstra(graph, n)
    print('closedge:' ,closedge)
    print('vertex:' , vertex)
    print('distance:' ,  distance)
