data = input()
ans = ['U', 'C', 'P', 'C']
check = 0
cnt = 0

for i in data:
    if i == ans[check]:
        cnt += 1
        check += 1
    if cnt == 4:
        break
if cnt == 4:
    print('I love UCPC')
else:
    print("I hate UCPC")
