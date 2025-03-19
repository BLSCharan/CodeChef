t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b=sum(a)
    c=[]
    for i in range(len(a)):
        c.append(max(0,a[i]-y))
    d=sum(c)
    e=d+x
    if e<b:
        print("COUPON")
    else:
        print("NO COUPON")
  

