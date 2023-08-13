n = int(input())
lst = []
level_sum = 0
stat_sum = 0
cnt = 0
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse = True)
for i in lst:
    if cnt == 42:
        break
    if i >= 250:
        level_sum += i
        stat_sum += 5
    elif i >= 200:
        level_sum += i
        stat_sum += 4
    elif i >= 140:
        level_sum += i
        stat_sum += 3
    elif i >= 100:
        level_sum += i
        stat_sum += 2   
    elif i >= 60:
        level_sum += i
        stat_sum += 1
    else:
        level_sum += i
    cnt += 1
print(level_sum, stat_sum)