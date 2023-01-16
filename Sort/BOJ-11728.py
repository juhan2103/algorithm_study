import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
answer = a + b
answer.sort()
for i in answer:
    print(i, end=' ')
