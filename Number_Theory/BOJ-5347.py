def gcd(a, b):
  while b != 0:
    remain = b
    b = a % b
    a = remain
  return a
def lcm(a, b):
  re_a = a // gcd(a, b)
  re_b = b // gcd(a, b)
  print(gcd(a, b) * re_a * re_b)
n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  lcm(a, b)