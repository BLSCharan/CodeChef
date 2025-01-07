t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    r=(a+b)/2
    if r>c:
        print("YES")
    else:
        print("NO")
    t-=1
