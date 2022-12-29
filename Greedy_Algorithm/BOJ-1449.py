n, l = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 배열을 오름차순으로 정렬
start = num_list[0]  # 시작 지점을 start 변수에 저장
count = 1  # count는 1로 시작
for data in num_list[1:]:  # start부터기 때문에 [1:]로 시작
    if data in range(start, start + l):  # 범위는 start + 테이프 길이만큼
        continue
    else:  # 더이상 이어지지 않으면 start 지점을 다시 지정
        start = data
        count += 1
print(count)
