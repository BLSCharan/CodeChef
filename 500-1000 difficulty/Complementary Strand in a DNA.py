t = int(input())

for _ in range(t):
    n = int(input())  
    s = input().strip()  
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    result = ""
    for c in s:
        result += complement[c]

    print(result)

