t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    a=x+y+z
    if a<2:
        print("Water filling time")
    else:
        print("Not now")
