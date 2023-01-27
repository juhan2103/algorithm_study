total = 0
lst = []
result_idx = []
for i in range(8):
    lst.append(int(input()))
for i in range(5):
    total += max(lst)
    idx = lst.index(max(lst))
    result_idx.append(idx+1)
    lst[idx] = 0
print(total)
for i in sorted(result_idx):
    print(i, end=' ')
