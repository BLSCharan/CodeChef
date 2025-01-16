from math import ceil
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x-y
    a=z/4
    if x<y:
        print(0)
    else:
        print(ceil(a))
