t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    z=x*y
    if z>=n:
        print("YES")
    else:
        print("NO")
