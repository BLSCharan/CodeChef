t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x=a-c
    y=b-d
    if x<y:
        print("First")
    elif x>y:
        print("Second")
    else:
        print("Any")
