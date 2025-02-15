t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x*3
    if z<=y:
        print("YES")
    else:
        print("NO")
