import numpy as np

_A = [[1,2,3],[4,5,6],[7,8,9]]
_B = [[7,9,1],[3,1,2],[2,4,5]]
A = np.array(_A)
B = np.array(_B)

print(A)
print(B)
print(A@B)
print(A*B)