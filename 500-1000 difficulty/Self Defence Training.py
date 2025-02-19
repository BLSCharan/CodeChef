t=int(input())
while t>0:
    x =int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(x):
        if 10<=l[i]<=60:
            c+=1
    print(c)
    t-=1
