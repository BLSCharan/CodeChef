t=int(input())
while(1<=t):
    x,a,b=map(int,input().split())
    c=a*1
    d=b*2
    e=c+d
    if e>=x:
        print("Qualify")
    else:
        print("NotQualify")
    t-=1
