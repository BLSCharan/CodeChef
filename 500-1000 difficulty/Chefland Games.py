t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    z=a+b+c+d
    if z==0:
        print("IN")
    else:
        print("OUT")
