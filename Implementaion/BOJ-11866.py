from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
result = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())  # 1,2번을 popleft시킨것을 후순위로 미룸
    result.append(queue.popleft())  # 3번째 요소를 result에 추가

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')
