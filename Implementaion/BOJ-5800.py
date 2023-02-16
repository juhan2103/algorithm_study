n = int(input())
cnt = 1
for i in range(n):
  lst = list(map(int,input().split()))
  lst.pop(0)
  lst.sort(reverse = True)
  gap = 0
  for j in range(1,len(lst)):
    if gap < lst[j-1] - lst[j]:
      gap = lst[j-1] - lst[j]
  print('Class', cnt)
  print('Max', str(max(lst)) + ',', 'Min', str(min(lst))+',', 'Largest gap', gap, )
  cnt += 1