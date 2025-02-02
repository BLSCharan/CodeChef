t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x-y
    if z<0:
        print("0")
    else:
        print(z)

