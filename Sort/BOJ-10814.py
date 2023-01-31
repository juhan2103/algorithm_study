import sys
n = int(sys.stdin.readline())
people = []
for i in range(n):
    people.append(input().split())
people.sort(key=lambda x: int(x[0]))
for person in people:
    print(person[0], person[1])
