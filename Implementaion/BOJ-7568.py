n = int(input())  # n을 입력받는다
people = []  # x, y를 입력받을 리스트 선언
for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y))
for i in people:
    rank = 1  # rank를 1로 초기화해준다
    for j in people:  # j번 만큼 비교를 하여 등수 비교를 한다
        if i[0] < j[0] and i[1] < j[1]:  # 다음 사람과 비교해서 덩치가 크면 rank를 1단계 높인다
            rank += 1
    print(rank, end=' ')
