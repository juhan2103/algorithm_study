import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int,input().split()))
for i in range(1, n):
  n_list[i] = n_list[i-1] + n_list[i]
n_list.insert(0,0)
for i in range(m):
  start, end = map(int, input().split())
  print(n_list[end] - n_list[start - 1])