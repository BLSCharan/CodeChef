t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n<k:
        print("Yes")
    else:
        print("No")
