if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    n = int(input().strip())
    
    is_strict_superset = True
    
    for _ in range(n):
        other_set = set(map(int, input().split()))
        
        if not (set_a.issuperset(other_set) and len(set_a) > len(other_set)):
            is_strict_superset = False
            break
            
    print(is_strict_superset)