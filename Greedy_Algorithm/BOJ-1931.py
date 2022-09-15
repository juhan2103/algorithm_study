n = int(input())  # n을 입력받는다
meet_time = []  # 회의 시간을 입력받을 리스트 선언
count = 1  # 첫번째 회의 count를 1로 미리 선언
for i in range(n):  # n만큼 반복
    a, b = map(int, input().split())  # 회의 시작 시간과 종료 시간을 입력받는다
    meet_time.append([a, b])  # 리스트에 회의 시간을 추가한다
meet_time.sort(key=lambda x: x[0])  # 시작 시간 오름차순 정렬
meet_time.sort(key=lambda x: x[1])  # 종료 시간 오름차순 정렬
max_time = meet_time[0][1]  # 최대 종료 시간을 저장한다
for i in range(1, n):
    if meet_time[i][0] >= max_time:  # 저장한 최대 종료시간보다 다음 시작시간이 더 클때
        count += 1  # count 증가
        max_time = meet_time[i][1]  # 최대 종료시간을 다시 저장
print(count)
