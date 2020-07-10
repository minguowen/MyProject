I=float('inf')      #无穷大
N = 4

#进行Floyd算法
class Solution():
    def floyd(self, graph, path, path_value, N):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        path[i][j][1:-1] = path[i][k][1:-1].copy()
                        path[i][j].insert(-1, k)

                        path_value[i][j] = path_value[i][k].copy()
                        path_value[i][j].append(graph[k][j])

        return graph, path, path_value


if __name__ == '__main__':
    a = Solution()

    graph = [
            [0, 2, 6, 4],
            [I, 0, 3, I],
            [7, I, 0, 1],
            [5, I, 12, 0]
        ]
    #记录路径
    path = [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[1, 0], [1, 1], [1, 2], [1, 3]],
        [[2, 0], [2, 1], [2, 2], [2, 3]],
        [[3, 0], [3, 1], [3, 2], [3, 3]],
    ]
    # 记录路径上面的值
    path_value = [
        [[0], [2], [2], [4]],
        [[], [0], [3], []],
        [[7], [], [0], [1]],
        [[5], [], [12], [0]],
    ]

    # 输出原始图
    print("Graph:")
    for i in range(N):
        print(graph[i])
    print('\n')

    graph, path, path_value = a.floyd(graph, path, path_value, N)
    #输出最短路径表
    print ("Shortest distance:")
    for i in range(N):
        print(graph[i])

    print('\n')
    #输出路径
    print ("Path:")
    for i in range(N):
        print(path[i])

    print('\n')
    #输出最短路径上的距离
    print ("Path_value:")
    for i in range(N):
        print(path_value[i])

