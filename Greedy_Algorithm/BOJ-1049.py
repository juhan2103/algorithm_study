n, m = map(int, input().split())
pricePackage = [[0] for _ in range(m)]
priceOne = [[0] for _ in range(m)]

for i in range(m):
    package, one = map(int, input().split())
    pricePackage[i] = package
    priceOne[i] = one

minPackage = min(pricePackage)
minOne = min(priceOne)

numOfPackage, numOfOne = 0, 0
if minOne * 6 >= minPackage:
    numOfPackage = n // 6
    numOfOne = n % 6
    if minPackage <= numOfOne * minOne:
        numOfPackage += 1
        numOfOne = 0

else:
    numOfOne = n

print(numOfPackage * minPackage + numOfOne * minOne)
