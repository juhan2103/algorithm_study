n = int(input())
vote = []
count = 0

for i in range(n):
    vote.append(int(input()))

dasom = vote[0]
votes = vote[1:]
votes.sort(reverse=True)
if n == 1:
    print(0)
else:
    while votes[0] >= dasom:
        dasom += 1
        votes[0] -= 1
        count += 1
        votes.sort(reverse=True)
    print(count)
