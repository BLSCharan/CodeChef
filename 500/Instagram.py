t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x>y*10:
        print("YES")
    else:
        print("NO")
