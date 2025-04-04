T = int(input())
for _ in range(T):
    N = int(input())
    difficulties = list(map(int, input().split()))
    to_remove = sum(1 for d in difficulties if d >= 1000)
    print(to_remove)

   
   
