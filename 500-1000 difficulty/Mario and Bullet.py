t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    a=y//x
    b=z-a
    if b<0:
        print("0")
    else:
        print(b)
