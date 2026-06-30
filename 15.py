if __name__ == '__main__':
    t = int(input().strip())
    
    for _ in range(t):
        num_elements_a = int(input().strip())
        set_a = set(map(int, input().split()))
        
        num_elements_b = int(input().strip())
        set_b = set(map(int, input().split()))
        
        print(set_a.issubset(set_b))