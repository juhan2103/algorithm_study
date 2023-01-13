earth, sun, moon = map(int, input().split())
e, s, m = 1, 1, 1
count = 1
while True:
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    if earth == e and sun == s and monn == m:
        print(count)
        break
    count += 1
    e += 1
    s += 1
    m += 1
