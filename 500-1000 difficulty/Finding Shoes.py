t = int(input())  
for _ in range(t):
    n, m = map(int, input().split())
    print(max(n, 2 * n - m))
