t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x=a*10
    y=b*5
    if x>y:
        print("FIRST")
    elif y>x:
        print("SECOND")
    else:
        print("ANY")
