t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split())
    if (x1+y1)<(x2+y2):
        print(x1+y1)
    else:
        print(x2+y2)

