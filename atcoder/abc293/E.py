import numpy as np
def mat_pow(A, b, m):
  R = np.eye(2,2, dtype=np.int64)
  while b > 0:
    if b & 1 == 1:
      R = np.matmul(R, A) % m

    A = np.matmul(A, A) % m
    b >>= 1

  return R

A, X, M = (int(x) for x in input().split())
B = np.array([[A, 1], [0, 1]], dtype=np.int64)
P = mat_pow(B, X, M)
# print(P)
print(P[0][1])
