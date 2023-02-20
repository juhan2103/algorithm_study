a = []
for i in range(5):
  a.append(int(input()))
result = sum(a) / 5
a.sort()
print(int(result))
print(a[2])