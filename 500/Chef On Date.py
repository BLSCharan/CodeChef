t=int(input())
while(1<=t):
    x,y=map(int,input().split())
    if x>=y:
        print("YES")
    else:
        print("NO")
    t-=1

