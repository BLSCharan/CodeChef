t=int(input())
while 1<=t:
    x=int(input())
    if x<4:
        print("MILD")
    elif 4<=x<7:
        print("MEDIUM")
    else:
        print("HOT")
    t-=1
