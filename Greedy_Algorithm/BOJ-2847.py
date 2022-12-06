n = int(input())
level = []
count = 0
for i in range(n):
    level.append(int(input()))
level.reverse()
for i in range(1, len(level)):
    dif = 0
    if level[i] >= level[i-1]:
        dif = level[i] - level[i-1] + 1
        count += dif
        level[i] -= dif
print(count)
