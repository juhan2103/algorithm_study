n, k = map(int, input().split())
arr = [False] * (n+1)
count = 0
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if arr[j] == False:
            arr[j] = True
            count += 1
            if count == k:
                print(j)
                break
