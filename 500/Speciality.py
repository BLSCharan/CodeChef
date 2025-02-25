t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print("Setter")
    elif b>c and b>a:
        print("Tester")
    else:
        print("Editorialist")
