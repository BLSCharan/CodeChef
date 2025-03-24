t = int(input())  

for _ in range(t):
    n = int(input()) 
    d = list(map(int, input().split())) 

    for i in range(1, n):
        if d[i] < d[i - 1]:
            print("No")
            break
    else:
        print("Yes")

