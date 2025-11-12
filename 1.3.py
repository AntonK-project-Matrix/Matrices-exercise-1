import numpy as np
import scipy.linalg as la

A = np.array([[7, 2],[3, 6]])
B = np.array([[2, -2],[1, 3]])
C = np.array([[1, 2, 3],[4, -6, 7], [1, 8, 9]])
D = np.array([[4, 5, 6],[3, -1, 2], [1, 6, 4]])

det_A = la.det(A)
det_B = la.det(B)
det_C = la.det(C)
det_D = la.det(D)

for x in [A, B, C, D]:
    eigenvalues, eigenvectors = la.eig(x)
    print(eigenvalues)
    print(eigenvectors)
