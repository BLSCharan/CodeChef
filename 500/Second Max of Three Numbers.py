t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    b=sorted([a,b,c])
    print(b[1])
