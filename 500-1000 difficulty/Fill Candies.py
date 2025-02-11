import math
t=int(input())
for _ in range(t):
    n,k,m=map(int,input().split())
    print(math.ceil(n/(k*m)))
