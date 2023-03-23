from collections import deque
def dfs(v):
  dfs_visited[v] = True
  print(v, end = ' ')
  for i in range(1, n+1):
    if not dfs_visited[i] and graph[v][i] == True:
      dfs(i)
      
def bfs(start):
  queue = deque([start])
  bfs_visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end= ' ')
    for i in range(1, n+1):
      if not bfs_visited[i] and graph[v][i] == True:
        queue.append(i)
        bfs_visited[i] = True
        
n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for i in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = True
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
dfs(v)
print()
bfs(v)