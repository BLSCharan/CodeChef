t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=x*5
    if a<y:
        print("NO")
    else:
        print("YES")

