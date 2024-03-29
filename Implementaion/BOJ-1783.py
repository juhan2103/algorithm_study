n, m = map(int, input().split())  # n은 세로 m은 가로 첫 시작은 (1, 1)
if n == 1:  # 세로의 길이가 1이면 아무곳도 이동 못함
    print(1)
elif n == 2:  # 세로의 길이가 2면 모든 움직임이 불가능하기 때문에 최대 4
    print(min(4, (m+1) // 2))
else:  # 세로의 길이가 2보다 크면
    if m <= 6:  # 가로의 길이가 6보다 작으면
        print(min(4, m))  # 모든 움직임을 사용 불가하기 때문에 최대치가 4
    else:
        print(m-2)  # 아닐 경우 m-2만큼 최대 개수가 나온다
