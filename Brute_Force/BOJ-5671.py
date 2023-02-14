while 1:
    try:
        n, m = map(int,input().split())
    except:
        break
    cnt = 0
    for num in range(n,m+1):
        result = set()
        s_num = str(num)
        for char in s_num:
            result.add(char)
        if len(s_num) == len(result):
            cnt += 1
    
    print(cnt)
    