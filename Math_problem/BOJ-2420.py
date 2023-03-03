n, m = map(int,input().split())
result = 0
if n > m:
  result = n - m
else:
  result = m - n
print(result)