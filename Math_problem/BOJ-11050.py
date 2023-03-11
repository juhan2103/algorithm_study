n, k = map(int, input().split())
count = k
result = 1
divide = 1
for i in range(count):
  result *= n
  divide *= k
  n -= 1
  k -= 1
print(result // divide)