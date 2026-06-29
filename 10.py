import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    array = np.array(matrix)
    
    min_axis_1 = np.min(array, axis=1)
    
    result = np.max(min_axis_1)
    
    print(result)