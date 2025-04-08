t=int(input())
v={'a','e','i','o','u'}
while(1<=t):
    hard=False
    c=0
    n=int(input())
    s=input().strip()
    for i in s:
        if i not in v:
            c+=1
            if c>=4:
                hard=True
                break
        else:
            c=0
    if hard:
        print("NO")  
    else:
        print("YES")
    t-=1
