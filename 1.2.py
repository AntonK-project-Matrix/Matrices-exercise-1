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

print("Determinants: ")
print(det_A)
print(det_B)
print(det_C)
print(det_D)
print("Inverses: ")

try:
    inv_A = la.inv(A)
    print(inv_A)
except:
    print("No inverse exists")

try:
    inv_B = la.inv(B)
    print(inv_B)
except:
    print("No inverse exists")

try:
    inv_C = la.inv(C)
    print(inv_C)
except:
    print("No inverse exists")

try:
    inv_D = la.inv(D)
    print(inv_D)
except:
    print("No inverse exists")
