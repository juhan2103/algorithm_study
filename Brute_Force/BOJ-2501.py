n, k = map(int,input().split())
n_list = []
for i in range(1, n+1):
  if n % i == 0:
    n_list.append(n // i)
n_list.sort()
if k > len(n_list):
  print(0)
else:
  print(n_list[k-1])