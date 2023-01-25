def gcd(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a


n = int(input())
lst = list(map(int, input().split()))
first = lst.pop(0)
for i in lst:
    num = gcd(first, i)
    print(str(first // num) + "/" + str(i // num))
