t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    print(min(y,x-y))
