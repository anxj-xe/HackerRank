import numpy as np

if __name__ == '__main__':
    n = int(input().strip())
    
    matrix_A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_A.append(row)
        
    matrix_B = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_B.append(row)
        
    A = np.array(matrix_A)
    B = np.array(matrix_B)
    
    result = np.dot(A, B)
    
    print(result)