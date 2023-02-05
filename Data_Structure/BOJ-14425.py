import sys
n, m = map(int, sys.stdin.readline().split())
s = set()
count = 0
for i in range(n):
    s.add(input())
for i in range(m):
    x = input()
    if x in s:
        count += 1
print(count)
