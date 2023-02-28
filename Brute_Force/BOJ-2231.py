n = int(input())
result = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    a_sum = i + sum(a)
    if a_sum == n:
        result = i 
        break
print(result)