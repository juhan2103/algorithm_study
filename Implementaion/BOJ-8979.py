n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # 금, 은, 동 순으로 정렬

grade, s = 1, 0  # s는 동률일 때 카운트 해주는 변수
for i in range(n):
    if i != 0:  # i가 0이 아닐때
        if medals[i-1][1:] == medals[i][1:]:  # 동률이면 count를 1 늘림
            s += 1
        else:
            if s:  # 동률이 있었다면
                grade += s  # grade에 count를 더해줌
                s = 0
            grade += 1
    if medals[i][0] == k:
        print(grade)
        break
