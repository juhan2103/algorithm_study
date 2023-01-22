n, k = map(int, input().split())
queue = [i+1 for i in range(n)]
lst = []
num = 0
for i in range(n):
    num += (k - 1)
    if num >= len(queue):
        num %= len(queue)
    lst.append(queue.pop(num))
print("<", ", ".join(str(i) for i in lst), ">", sep="")
