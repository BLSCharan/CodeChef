t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if(x%3>0):
        print(x*y+z*(x//3))
    else:
        print(x*y+z*(x//3-1))
