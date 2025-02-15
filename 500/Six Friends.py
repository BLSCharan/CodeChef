t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=3*x
    b=2*y
    if a<b:
        print(a)
    else:
        print(b)
