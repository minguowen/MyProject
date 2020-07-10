#A Naïve Implementation of Kruskal’s Algorithm
class Kruskal():
    def naive_find(self, C, u):  # Find component rep.
        while C[u] != u:  # Rep. would point to itself
            u = C[u]
        return u

    def naive_union(self, C, u, v):
        u = self.naive_find(C, u)                        # Find both reps
        v = self.naive_find(C, v)
        C[u] = v                                    # Make one refer to the other

    def naive_kruskal(self, G):
        E = [(G[u][v],u,v) for u in G for v in G[u]]
        T = set()                                   # Empty partial solution
        C = {u:u for u in G}                        # Component reps
        for _, u, v in sorted(E):                   # Edges, sorted by weight
            if self.naive_find(C, u) != self.naive_find(C, v):
                T.add((u, v))                       # Different reps? Use it!
                self.naive_union(C, u, v)                # Combine components
        return T

if __name__ == '__main__':
    a = Kruskal()
    G = {
        0: {1:1, 2:3, 3:4},
        1: {2:5},
        2: {3:2},
        3: set()
        }
    print(list(a.naive_kruskal(G)))
    #[(0, 1), (2, 3), (0, 2)]