t=int(input())
for _ in range(t):
    a,x,b,y=map(int,input().split())
    p=a/x
    q=b/y
    if q>p:
        print("Bob")
    elif p>q:
        print("Alice")
    else:
        print("Equal")
