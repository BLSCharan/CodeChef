t=int(input())
while(1<=t):
    x=int(input())
    if x<3:
        print("LIGHT")
    elif 3<=x<7:
        print("MODERATE")
    elif x>=7:
        print("HEAVY")
    t-=1
