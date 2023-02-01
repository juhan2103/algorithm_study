import sys
n, m = map(int, sys.stdin.readline().split())
a = set()
b = set()
for i in range(n):
    a.add(sys.stdin.readline())
for i in range(m):
    b.add(sys.stdin.readline())
result = sorted(list(a & b))
print(len(result))
print(''.join(result), end='')
