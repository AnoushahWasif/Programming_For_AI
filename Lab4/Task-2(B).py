graph = {
  'A' : ['B','C','D'],
  'B' : ['C', 'E'],
  'E' : ['A'],
  'C' : ['E'],
  'D' : ['F', 'C'],
  'F' : ['C'],
  'G' : ['F','H','D'],
  'H' : ['C']
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')
