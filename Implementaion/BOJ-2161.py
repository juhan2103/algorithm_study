from collections import deque
n = int(input())
queue = deque(list(range(1, n+1)))
while queue:
    card = queue.popleft()
    print(card, end=' ')
    if queue:
        card = queue.popleft()
        queue.append(card)
