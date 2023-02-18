n, m = map(int,input().split())
n_list = []
m_list = []
for i in range(n):
  n_list.append(list(map(int,input().split())))
for i in range(n):
  m_list.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m):
    print(n_list[i][j] + m_list[i][j], end = ' ')
  print()