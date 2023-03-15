n = int(input())
people = list(map(int, input().split()))
if people.count(0) >= len(people) / 2:
  print('INVALID')
elif people.count(1) > people.count(-1):
  print('APPROVED')
else:
  print('REJECTED')