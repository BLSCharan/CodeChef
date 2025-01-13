t=int(input())
while 1<=t:
    x,y=map(int,input().split())
    z=x/2
    if y>=z:
        print("YES")
    else:
        print("NO")
    t-=1
