n, b = map(int, input().split())
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while n != 0:
    answer += str(alpha[n % b])
    n = n // b
print(answer[::-1])
    