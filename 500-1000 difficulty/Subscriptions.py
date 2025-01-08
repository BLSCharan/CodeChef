from math import ceil
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    s=ceil(x/6)
    print(s*y)
    
