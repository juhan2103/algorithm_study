import sys
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, sys.stdin.readline().split)))
xy.sort(key=lambda x: (x[0], x[1]))
for i in xy:
    print(i[0], i[1])
