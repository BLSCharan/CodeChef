t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    z=n//2
    x=n-z
    print((z*a)+(x*b))
    
