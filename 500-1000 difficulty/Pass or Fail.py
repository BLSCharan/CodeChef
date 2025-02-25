t=int(input())
for _ in range(t):
    n,x,p=map(int,input().split())
    a=n-x
    b=a*(-1)
    c=x*3
    d=(b+c)
    if d>=p:
        print("PASS")
    else:
        print("FAIL")
    
    
