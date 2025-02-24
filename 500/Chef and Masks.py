t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=x*100
    b=y*10
    if a<b:
        print("Disposable")
    else:
        print("Cloth")
