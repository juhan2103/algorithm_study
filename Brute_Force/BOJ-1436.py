n = int(input())
count = 0
n_count = 666
while True:
    if '666' in str(n_count):
        count += 1
    if count == n:
        print(n_count)
        break
    n_count += 1
