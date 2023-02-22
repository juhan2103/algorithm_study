n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]
for i in range(m):
  x, y = map(int, input().split())
  tmp = n_list[x-1]
  n_list[x-1] = n_list[y-1]
  n_list[y-1] = tmp
for i in n_list:
  print(i, end = ' ')