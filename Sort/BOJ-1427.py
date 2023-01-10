x = input()
lst = []
for i in x:
    lst.append(int(i))
lst.sort(reverse=True)
for i in lst:
    print(str(i), end='')
