import sys
input = sys.stdin.readline
from collections import deque
def bfs(start):
  queue = deque([start])
  visited[start] = 1
  global count
  while queue:
    v = queue.popleft()
    graph[v].sort()
    for i in graph[v]:
      if not visited[i]:
        count += 1
        queue.append(i)
        visited[i] = count

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [0] * (n + 1)
count = 1
bfs(v)
for i in visited[1:]:
  print(i)