t=int(input())
while(1<=t):
    x,y,z=map(int,input().split())
    a=x*y
    b=a/2
    if z>b:
        print("YES")
    else:
        print("NO")
    t-=1
