t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    happy_days = 0

    for i in range(n):
        if a[i] <= 2 * b[i] and b[i] <= 2 * a[i]:
            happy_days += 1

    print(happy_days)
    
