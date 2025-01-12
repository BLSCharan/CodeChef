from math import ceil

t = int(input())
while 1 <= t:
    x, y = map(int, input().split())
    z = x * y
    print(ceil(z / 4))
    t -= 1
