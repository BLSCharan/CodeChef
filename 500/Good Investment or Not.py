t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=y*2
    if x>=z:
        print("YES")
    else:
        print("NO")
