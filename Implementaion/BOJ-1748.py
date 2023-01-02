n = input()
count = len(n) - 1
answer = 0
for i in range(count):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += (int(n) - (10 ** count) + 1) * (count + 1)
print(answer)
