import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=math.ceil(y/100)
    if a>x:
        print(a-x)
    else:
        print("0")
