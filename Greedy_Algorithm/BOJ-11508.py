import sys
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
n_list.sort(reverse = True)
result = 0
for i in range(n):
    if i % 3 != 2:
        result += n_list[i]
print(result)