from collections import deque
n, m = map(int, input().split())
idx_list = list(map(int, input().split()))
count = 0
queue = deque([i+1 for i in range(n)])
for idx in idx_list:
    while True:
        if queue[0] == idx:
            queue.popleft()
            break
        else:
            if queue.index(idx) < len(queue) / 2:
                while queue[0] != idx:
                    queue.append(queue.popleft())
                    count += 1
            else:
                while queue[0] != idx:
                    queue.appendleft(queue.pop())
                    count += 1
print(count)
