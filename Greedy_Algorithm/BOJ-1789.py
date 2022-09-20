s = int(input())
sum = 0
count = 0
while True:
    count += 1
    sum += count
    if sum > s:  # sum이 s보다 커질때 break
        break
print(count-1)
