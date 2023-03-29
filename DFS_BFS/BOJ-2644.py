import sys
from collections import deque
def bfs(start):
  queue = deque([start])  
  visited[start] = 1
  while queue:
    v = queue.popleft()
    if v == end:
      break
    for i in graph[v]:
      if not visited[i]:
        visited[i] = visited[v] + 1
        queue.append(i)
      
input = sys.stdin.readline
n = int(input())
start, end = map(int, input().split())
m  = int(input())
graph = [[] for i in range(n + 1)]
for i in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
visited = [0] * (n + 1)
bfs(start)
if visited[end] == 0:
  print(-1)
else:
  print(visited[end] - 1)