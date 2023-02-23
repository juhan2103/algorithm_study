import sys
n, m = map(int, sys.stdin.readline().split())
n_list = [i+1 for i in range(n)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  n_list[a-1:b] = n_list[a-1:b][::-1]
print(*n_list)