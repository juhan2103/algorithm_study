from itertools import combinations
d = [int(input()) for _ in range(9)]
for i in combinations(d, 7):
    if sum(i) == 100:
        n = i
        break
print('\n'.join(map(str, sorted(i))))