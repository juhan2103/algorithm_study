n = int(input())  # n을 입력받는다
numbers = []  # 숫자를 입력받을 리스트를 선언
for i in range(n):  # n만큼 반복
    num = int(input())  # 숫자를 입력받는다
    numbers.append(num)  # 입력받은 숫자를 리스트 안에 저장
numbers.sort()  # 오름차순으로 정렬
for i in numbers:
    print(i)  # 오름차순으로 출력
