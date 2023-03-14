t = int(input())
for i in range(t):
  sentense = list(input().split())
  for j in range(len(sentense)):
    print(sentense[j][::-1], end = ' ')