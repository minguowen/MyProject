inf = float('inf')


def prim(graph, n):
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
        mini = inf
        for i in range(n):
            if mini > closedge[i] and not flag[i]:
                mini = closedge[i]
                k = i
        if k == 0:  # 不连通
            return
        flag[k] = True
        vertex.append(k)
        distance.append(closedge[k])
        for i in range(n):
            if closedge[i] > graph[k][i] and not flag[i]:
                closedge[i] = graph[k][i]
    return closedge, vertex, distance


if __name__ == '__main__':
    n = 6
    graph = [
            [  0,   6,   3, inf, inf, inf],
            [  6,   0,   2,   5, inf, inf],
            [  3,   2,   0,   3,   4, inf],
            [inf,   5,   3,   0,   2,   3],
            [inf, inf,   4,   2,   0,   5],
            [inf, inf, inf,   3,   5,   0],
            ]
    closedge, vertex, distance = prim(graph, n)
    print('closedge:' ,closedge)
    print('vertex:' , vertex)
    print('distance:' ,  distance)
