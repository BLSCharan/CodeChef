t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=n/2
    if x>=a:
        print("YES")
    else:
        print("NO")
