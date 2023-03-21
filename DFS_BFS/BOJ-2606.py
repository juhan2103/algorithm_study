def dfs(v):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
            count += 1
    
n = int(input())
m = int(input())
count = 0
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
dfs(1)
print(count)