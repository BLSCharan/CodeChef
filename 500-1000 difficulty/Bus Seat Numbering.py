t=int(input())
while(1<=t):
    n=int(input())
    if n<=10:
        print("Lower Double")
    elif 10<n<=15:
        print("Lower Single")
    elif 15<n<=25:
        print("Upper Double")
    else:
        print("Upper Single")
    t-=1
