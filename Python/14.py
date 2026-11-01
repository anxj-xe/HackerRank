import numpy as np

if __name__ == '__main__':
    coefficients = list(map(float, input().split()))
    x = float(input().strip())
    
    result = np.polyval(coefficients, x)
    
    print(result)