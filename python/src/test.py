import numpy as np

coefficients = np.array([
    [109.66, 110.04, 110.23, 110.47, 110.77, 110.95, 111.29, 111.5, 111.41, 111.55, 112.22, 112.76, 106.37, 108.25, 108.26, 108.25, 108.15, 107.85, 108.24, 108.99, 109.12, 108.93, 109.17, 109.57],  
    [108.39, 110.22, 109.69, 109.34, 109.59, 110.66, 112.43, 113.93, 114.11, 114.22, 113.88, 113.93, 110.25, 112.26, 109.79, 109.51, 109.46, 109.26, 110.29, 111.37, 111.04, 108.76, 108.33, 108.49],  
    [110.13, 111.97, 112.06, 112.63, 113.08, 113.81, 115.27, 116.1, 116.47, 116.72, 116.98, 117.29, 107.53, 108.62, 108.37, 108.53, 108.86, 108.93, 109.05, 109.26, 109.31, 109.5, 109.75, 109.92],  
    [105.25, 105.63, 105.69, 105.92, 106.27, 106.64, 107.06, 107.34, 107.48, 107.85, 108.13, 108.62, 102.43, 103.35, 102.97, 103.11, 103.2, 103.31, 103.5, 103.73, 103.9, 104.1, 104.44, 104.65],  
    [103.13, 103.2, 103.33, 103.45, 103.64, 103.81, 104.14, 104.32, 104.49, 104.7, 104.94, 105.36, 102.23, 102.49, 102.29, 102.29, 102.28, 102.28, 102.25, 102.22, 102.25, 102.38, 102.64, 102.87],  
    [103.54, 104.49, 106.05, 106.66, 106.52, 106.51, 107.03, 107.31, 108.32, 109.07, 110.13, 110.86, 100.03, 104.03, 104.28, 103.83, 104.25, 104.9, 105.83, 105.83, 103.72, 103.45, 103.93, 103.47],  
    [103.01, 103.21, 103.4, 103.73, 103.95, 104.27, 104.6, 104.83, 104.99, 105.12, 105.33, 105.57, 101.77, 101.98, 101.93, 102.04, 102.14, 102.24, 102.3, 102.3, 102.39, 102.45, 102.65, 102.83],  
    [102.53, 102.56, 102.63, 102.66, 102.69, 102.72, 102.77, 102.86, 102.9, 102.97, 103.03, 103.11, 102.28, 102.29, 102.31, 102.31, 102.32, 102.34, 102.37, 102.39, 102.42, 102.44, 102.48, 102.51],  
    [107.37, 109.89, 115.17, 114.49, 117.18, 121.42, 117.96, 111.46, 108.97, 106.6, 108.98, 105.95, 93.73, 95.18, 97.36, 98.21, 98.95, 100.01, 102.37, 102.31, 102.15, 104.71, 107.96, 106.12],  
    [97.94, 97.9, 97.92, 97.8, 97.81, 97.66, 97.91, 97.9, 97.86, 97.8, 97.77, 97.73, 98.59, 98.62, 98.49, 98.29, 98.14, 98.15, 98.11, 98.06, 98, 97.96, 97.99, 97.97],  
    [103.06, 103.58, 103.68, 104.67, 104.85, 104.92, 105.13, 106.67, 112.89, 115.55, 114.82, 115.19, 107.11, 107.11, 107.12, 107.15, 107.18, 107.21, 107.24, 107.28, 104.18, 104.44, 103.48, 103.03],  
    [98.89, 99.4, 99.61, 100.76, 101.5, 102.04, 102.84, 103.28, 103.32, 103.38, 103.6, 103.69, 99, 99.13, 99.1, 98.99, 98.76, 98.68, 98.58, 98.55, 98.56, 98.6, 98.69, 98.73],  
    [105.81, 106.04, 106.52, 106.71, 106.91, 107.17, 107.63, 107.85, 108, 108.26, 108.49, 108.74, 104.18, 104.94, 104.65, 104.73, 104.79, 104.85, 104.85, 104.85, 104.87, 104.99, 105.25, 105.4],  
    [141.43, 144.04, 150.54, 151.64, 150.85, 149.13, 145.57, 144.25, 141.78, 142.49, 145.08, 145.74, 141.53, 141.88, 137.66, 135.05, 137.31, 138.85, 136.92, 136.25, 136.25, 135.97, 139.57, 139.91],  
    [98.74, 98.47, 99.1, 99.17, 99.82, 100.54, 101.17, 101.35, 101.89, 103.77, 106.78, 104.01, 99.47, 99.3, 99.52, 99.82, 99.61, 99.31, 99.41, 98.97, 98.49, 98.44, 98.23, 99.05],  
])

I = np.array([
    [105.28],
    [106.33],
    [107.08],
    [107.28],
    [107.68],
    [108.42],
    [108.85],
    [108.85],
    [109.29],
    [109.44],
    [109.87],
    [109.85],
    [103.27],
    [104.84],
    [104.56],
    [104.52],
    [104.68],
    [104.88],
    [105.53],
    [105.79],
    [105.14],
    [104.93],
    [105.27],
    [105.08],
])


result = np.array([
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
])


print(f"{coefficients.shape}\n{result.shape}")

w = np.linalg.inv(coefficients - I) @ result
test = coefficients @ w

print(f"{w * 100}\n{test}\n{test - result}")