n = input()
num_list = []
count = [0 for i in range(10)]
for i in n:
    num_list.append(int(i))
for i in num_list:
    if i == 6 or i == 9:
        if count[6] > count[9]:
            count[9] += 1
        elif count[9] > count[6]:
            count[6] += 1
        elif count[6] == count[9]:
            count[6] += 1
    else:
        count[i] += 1
print(max(count))
