t=int(input())
while(1<=t):
    x,y=map(int,input().split())
    if y>=x and y%x==0:
        print("YES")
    else:
        print("NO")
    t-=1
 
