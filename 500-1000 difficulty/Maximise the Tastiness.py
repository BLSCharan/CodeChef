t=int(input())
while(1<=t):
    a,b,c,d=map(int,input().split())
    x=max(a,b)
    y=max(c,d)
    print(x+y)
    t-=1
