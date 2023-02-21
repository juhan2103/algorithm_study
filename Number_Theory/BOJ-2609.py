def gcd(a, b):
  while b != 0:
    remain = b
    b = a % b
    a = remain
  return remain
x, y = map(int,input().split())
print(gcd(x, y))
print(gcd(x, y) * (x // gcd(x, y)) * (y // gcd(x, y)))