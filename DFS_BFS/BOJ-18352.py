from collections import deque
import sys
def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
bfs(x)