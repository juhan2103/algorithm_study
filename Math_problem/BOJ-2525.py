a, b = map(int, input().split())
c = int(input())
b += c
if b // 60 >= 1:
  if a + (b // 60) >= 24:
    a += (b // 60) - 24
  else:
    a += b // 60
  b %= 60
print(a, b)