T = int(input())
for _ in range(T):
    K, X = map(int, input().split())
    remaining_days = (K * 7) - X
    print(remaining_days)
