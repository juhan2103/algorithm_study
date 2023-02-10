n = int(input())
m = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
left, right = 0, n-1
count = 0
while left < right:
    if n_list[left] + n_list[right] == m:
        left += 1
        count += 1
    elif n_list[left] + n_list[right] > m:
        right -= 1
    else:
        left += 1
print(count)
