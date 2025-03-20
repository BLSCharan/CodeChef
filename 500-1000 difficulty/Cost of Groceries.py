t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t=0
    for i in range(n):
        if a[i]>=x:
            t+=b[i]
    print(t)
            
            
    

