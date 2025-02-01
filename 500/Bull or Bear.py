t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("LOSS")
    elif x==y:
        print("NEUTRAL")
    else:
        print("PROFIT")
