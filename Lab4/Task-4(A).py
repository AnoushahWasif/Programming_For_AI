class Graph:
    def __init__(self,edges,n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
def DFS(graph, v, discovered):
    discovered[v] = True
    print(v, end=' ')
    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)
if __name__ == '__main__':
    edges = [
        (0,1), (0,3), (0,2), (1,3), (2,4),(3,5),
        (3,6), (5,2), (4,5), (4,7)
    ]
    n = 8
    graph = Graph(edges, n)
    discovered = [False] * n
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)


