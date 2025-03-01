t=int(input())
while 1<=t:
    s=0
    n=int(input())
    while n>0:
        s += n % 10 
        n //= 10
    print(s)
    t-=1
