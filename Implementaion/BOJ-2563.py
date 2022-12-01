n = int(input())
lst = [[0 for _ in range(101)] for _ in range(101)]

for k in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            lst[i][j] = 1

answer = 0
for i in lst:
    answer += i.count(1)
print(answer)
