from collections import deque
class Graph:
  def __init__(self,edges, n):

    self.adjList = [[] for _ in range(n)]

    for(src, dest) in edges:
      self.adjList[src].append(dest)
      self.adjList[dest].append(src)

def BFS(graph, v, discovered):
  q= deque()
  discovered[v] = True
  q.append(v)

  while q:
    v= q.popleft()
    print(v, end=' ')

    for u in graph.adjList[v]:
      if not discovered[u]:
        discovered[u]= True
        q.append(u)

if __name__ == '__main__':
    edges =[
      (1,2),(1,3),(2,6),(2,5) ]

    n= 7

    graph = Graph(edges, n)
    discovered = [False]* n

    for i in range(n):
       if not discovered[i]:
          BFS(graph,i,discovered)
