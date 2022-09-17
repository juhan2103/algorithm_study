n = int(input())
a_list = list(map(int,input().split())) # a와 b의 리스트를 입력 받는다
b_list = list(map(int,input().split()))
s = 0 # 최솟값 변수 선언
for i in range(n):
  s += min(a_list) * max(b_list) # a_list의 최솟값과 b_list의 최댓값을 곲한다
  a_list.remove(min(a_list)) # a_list의 최솟값을 제거
  b_list.remove(max(b_list)) # b_list의 최솟값을 제거
print(s)