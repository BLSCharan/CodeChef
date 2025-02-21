import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=math.ceil(x/10)
    b=math.ceil(y/10)
    print(abs(b-a))
