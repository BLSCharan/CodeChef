t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x=a*b
    y=c*d
    if y>=x:
        print("Yes")
    else:
        print("No")
