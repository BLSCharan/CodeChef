t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(list(set(a)))
    if len(b) >= 2:
        c = b[len(b) - 1] + b[len(b) - 2]
        print(c)
    t -= 1
