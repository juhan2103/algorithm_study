a, b = map(int, input().split())
n = int(input())
frequency_list = []
for i in range(n):
    frequency_list.append(int(input()))

x = abs(a-b)
min_count = []
min_count.append(x)

for i in range(n):
    min_count.append(abs(b-frequency_list[i])+1)
print(min(min_count))
