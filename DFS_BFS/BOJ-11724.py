import sys
from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
count = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            count += 1
        else:
            bfs(i)
            count += 1
print(count)