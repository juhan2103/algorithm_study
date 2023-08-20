n = int(input())
n_sum = 0
n_two_power = 0
n_three_power = 0
for i in range(1, n + 1):
    n_sum += i
    n_three_power += i * i * i
    
n_two_power = n_sum * n_sum
print(n_sum)
print(n_two_power)
print(n_three_power)