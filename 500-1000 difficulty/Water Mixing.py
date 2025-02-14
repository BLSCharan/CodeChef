t = int(input()) 
for _ in range(t):
    a, b, x, y = map(int, input().split())  
    if b >= a:  
        if b - a <= x:  
            print("YES")
        else:
            print("NO")
    else:
        if a - b <= y:  
            print("YES")
        else:
            print("NO")

