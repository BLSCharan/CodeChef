t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=500-a*2
    d=1000-(a+b)*4
    e=c+d
    f=1000-b*4
    g=500-(a+b)*2
    h=f+g
    print(max(e,h))
