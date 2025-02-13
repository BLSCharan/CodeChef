t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    c=x+y
    b=c//2
    if(b%2==0 ):
        print("Alice")
    else:
        print("bob")
