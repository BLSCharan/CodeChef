t = int(input())
vowels = {"a", "e", "i", "o", "u"}

for _ in range(t):
    s = input().strip().lower()
    count = 0

    for char in s:
        if char in vowels:
            count += 1
            if count > 2:
                print("Happy")
                break
        else:
            count = 0 
    else:
        print("Sad")

