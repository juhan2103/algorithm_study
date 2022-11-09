n = int(input())  # n을 입력받는다
distance = list(map(int, input().split()))  # 거리를 입력받는다
oil = list(map(int, input().split()))  # 각 도시의 기름값을 입력받는다

min_price = distance[0] * oil[0]  # 맨 처음 도착한 도시에서 다음 거리까지 기름을 충전함

min_cost = oil[0]  # 기름값의 최솟값을 저장

for i in range(1, n-1):  # 1부터 n-1까지
    if min_cost > oil[i]:  # 더 작은 oil값을 발견했을때
        min_cost = oil[i]   # 더 작은 값으로 변경
    min_price += min_cost * distance[i]  # 다음 거리까지의 기름을 충전

print(min_price)
