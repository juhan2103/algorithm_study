import sys
def gcd(a, b):
  while b != 0:
    remain = b
    b = a % b
    a = remain
  return a
def lcm(a, b):
  x = a // gcd(a, b)
  y = b // gcd(a, b)
  result = x * y * gcd(a, b)
  return result
n = int(sys.stdin.readline())
for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(lcm(a, b))