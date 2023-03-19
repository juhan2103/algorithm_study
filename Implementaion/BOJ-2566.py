max_list = []
for i in range(9):
  max_list.append(list(map(int, input().split())))
result = 0
row, column = 1, 1
for i in range(9):
  for j in range(9):
    if max_list[i][j] >= result:
      result = max_list[i][j]
      row = i
      column = j
print(result)
print(row+1, column+1)