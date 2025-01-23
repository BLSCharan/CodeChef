t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    a=x*y
    if z%y==0 and y<=a:
        print("YES")
    else:
        print("NO")

