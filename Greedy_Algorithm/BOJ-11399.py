n = int(input())  # n을 입력받는다
atm = list(map(int, input().split()))  # 사람들이 줄을 서는 순서를 입력받는다
atm.sort()  # 오름차순으로 리스트를 정렬한다
result = 0  # 결과값 변수 정의
for i in range(n):
    for j in range(i+1):  # i+1번 만큼 반복
        result += atm[j]  # 순번대로 필요한 시간의 합을 더한다
print(result)
