t=int(input())
for _ in range(t):
    x,y,d=map(int,input().split())
    a=abs(x-y)
    if d>=a:
        print("YES")
    else:
        print("NO")

