class Graph():

    def find_path(self, maps, start, end, path = []):
        path = path + [start]

        if start not in maps:
            return None

        if start == end:
            return path

        for node in maps[start]:
            if node not in path:
                newpath = self.find_path(maps, node, end, path)
                if newpath:
                    return newpath

        return None


    def find_all_path(self, maps, start, end, path=[]):
        path = path + [start]

        if start not in maps:
            return None

        if start == end:
            return path
        paths = []
        for node in maps[start]:
            if node not in path:
                newpaths = self.find_all_path(maps, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


    def find_shortest_path(self, maps, start, end, path=[]):
        path = path + [start]

        if start not in maps:
            return None

        if start == end:
            return path
        shortest = None
        for node in maps[start]:
            if node not in path:
                newpath = self.find_shortest_path(maps, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
                    else:
                        if len(newpath) == len(shortest):
                            for each in newpath:
                                shortest.append(each)
                        #   shortest.append(newpath) 作为列表增加进来
        return shortest


if __name__ == '__main__':

    maps = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    G = Graph()
    path = G.find_path(maps, 'A', 'D')
    print(path)
    path = G.find_all_path(maps, 'A', 'D')
    print(path)
    path = G.find_shortest_path(maps, 'A', 'D')
    print(path)