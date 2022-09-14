n, k = map(int, input().split())  # n, k를 입력받는다
coins = []  # n개의 coin을 입력받을 리스트를 선언
count = 0  # 최소 동전 개수 변수를 선언
for i in range(n):  # 동전을 입력받고 리스트에 넣는다
    num = int(input())
    coins.append(num)
coins.sort(reverse=True)  # 내림차순으로 다시 정렬
for coin in coins:  # 내림차순으로 정렬된 coin을 하나씩 비교
    if k // coin == 0:  # 몫이 0일 경우 넘어간다
        continue
    else:
        count += k // coin  # k를 coin으로 나눈 몫을 count에 더해준다
        k %= coin  # k를 coin으로 나눈 나머지를 다시 k에 저장한다
print(count)
