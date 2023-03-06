import math
n = int(input())
m = int(input())
result = []
for i in range(n, m+1):
  if math.sqrt(i) == int(math.sqrt(i)):
    result.append(i)
if len(result) == 0:
  print(-1)
else:
  print(sum(result))
  print(result[0])