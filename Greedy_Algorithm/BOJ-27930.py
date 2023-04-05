s = input()
korea_list = ['K','O','R','E','A']
yonsei_list = ['Y', 'O', 'N', 'S', 'E', 'I']
k_count = []
y_count = []
for i in s:
  if len(k_count) == 5:
    print('KOREA')
    break
  if len(y_count) == 6:
    print('YONSEI')
    break
  if i in korea_list and i not in k_count:
    k_count.append(i)
  if i in yonsei_list and i not in y_count:
    y_count.append(i)