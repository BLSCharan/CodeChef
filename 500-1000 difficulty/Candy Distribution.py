t=int(input())
while 1<=t:
    x,y=map(int,input().split())
    if x%y==0:
        z=x//y
        if z%2==0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    t-=1

