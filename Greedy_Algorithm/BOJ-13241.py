def gcd(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


a, b = map(int, input().split())
print(lcm(a, b))
