t=int(input())
while 1<=t:
    a,b=map(int,input().split())
    c=a+b
    d=21-c
    if c>10:
        print(d)
    else:
        print("-1")
    t-=1
