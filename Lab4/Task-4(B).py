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
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')
