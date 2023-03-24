def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1:
    global count
    graph[x][y] = 0
    count += 1
    dfs(x-1 ,y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
n = int(input())
graph = []
count_list = []
result = 0
count = 0
for i in range(n):
  graph.append(list(map(int, input())))
for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      result += 1
      count_list.append(count)
      count = 0
count_list.sort()
print(result)
for i in count_list:
  print(i)