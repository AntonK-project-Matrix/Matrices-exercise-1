import numpy as np
import scipy.linalg as la

n = int(input())

a = int(input())
b = int(input())

rows, cols = n, n
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        random_val = np.random.rand()
        row.append(random_val)
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        print(f"{matrix[i][j]}", end=" ")
    print()

eigenvalues, eigenvectors = la.eig(matrix)
print(eigenvalues)

for i, val in enumerate(eigenvalues):
    if a < val.real < b:
        print(f"λ{i+1}: In the interval")
    else:
        print(f"λ{i+1}: Not in the interval")
