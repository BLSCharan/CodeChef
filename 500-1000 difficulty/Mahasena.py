def is_ready_for_battle():
    n = int(input())
    
    weapons = list(map(int, input().split()))
    
    even_count = sum(1 for weapon in weapons if weapon % 2 == 0)
    odd_count = n - even_count  
    
    if even_count > odd_count:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")


is_ready_for_battle()

