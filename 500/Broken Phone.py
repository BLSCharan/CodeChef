t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a<b:
        print("REPAIR")
    elif a>b:
        print("NEW PHONE")
    else:
        print("ANY")
