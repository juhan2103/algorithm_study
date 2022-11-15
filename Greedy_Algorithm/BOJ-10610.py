n = int(input())
lst = []
for i in str(n):
    lst.append(i)
lst.sort(reverse=True)
answer = ''
for i in lst:
    answer += i
if int(answer) % 30 == 0:
    print(int(answer))
else:
    print(-1)
