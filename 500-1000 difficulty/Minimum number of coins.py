t=int(input())
for _ in range(t):
    x=int(input())
    if x%5!=0 and x%10!=0:
        print("-1")
    else:
         print(int((x//10)+(x%10)/5))
