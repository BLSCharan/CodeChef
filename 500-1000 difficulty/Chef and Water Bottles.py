t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    if (n*x)<k:
        print(n)
    else:
        print(k//x)
