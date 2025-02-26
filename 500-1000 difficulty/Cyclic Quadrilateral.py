t=int(input())
while(1<=t):
    a,b,c,d=map(int,input().split())
    if (a+c)==180:
        print("YES")
    else:
        print("NO")
    t-=1    
