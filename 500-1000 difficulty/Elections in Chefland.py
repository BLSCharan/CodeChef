t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    ages=list(map(int,input().split()))
    c=sum(1 for i in ages if i>=y)
    print(c)
