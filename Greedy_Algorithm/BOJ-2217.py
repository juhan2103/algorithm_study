n = int(input())  # n을 입력받는다
rope = []  # 입력받을 로프 리스트 선언
for i in range(n):
    num = int(input())
    rope.append(num)
rope.sort(reverse=True)  # 로프의 최대 중량을 내림차순으로 정렬
result = []  # 결과 리스트 선언
for i in range(len(rope)):
    result.append(rope[i]*(i+1))  # 로프의 개수에 로프의 최대 중량을 곱한다
print(max(result))  # 결과의 최댓값을 출력
