t=int(input())
while(1<=t):
    x=int(input())
    if x%3==2:
        print("SMALL")
    elif x%3==0:
        print("NORMAL")
    elif x%3==1:
        print("HUGE")
    t-=1
