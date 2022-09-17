n = int(input())  # n 입력받기
stack = []  # 스택 리스트 선언
sum = 0  # 스택의 합 변수 선언
for i in range(n):
    num = int(input())
    if num == 0:  # 0이 입력되면 최근 수를 지운다
        stack.pop()
    else:  # 0이 아닌 다른 수가 입력되면 스택에 추가
        stack.append(num)
for i in range(len(stack)):  # 리스트의 전체 합을 구한다
    sum += stack[i]
print(sum)  # 합계 출력
