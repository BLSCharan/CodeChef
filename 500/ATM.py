x, y = map(float, input().split())
if x % 5 == 0 and x + 0.50 <= y:
    y -= (x + 0.50)
print(f"{y:.2f}")

