import sys
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
left, right = 0, n-1
count = 0
while left < right:
  result = lst[left] + lst[right]
  if result == x:
    count += 1
    left += 1
  elif result < x:
    left +=1
  else:
    right -=1
print(count)