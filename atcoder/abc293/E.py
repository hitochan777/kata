def mat_pow(A, b, m):
  R = [[0,0],[0,0]]
  T = [[1,0],[0,1]]
  while b > 0:
    if b & 1 == 1:
      R = mat_mul(R, T, m)

    T = mat_mul(T, T, m)
    b >>= 1

A, X, M = (int(x) for x in input().split())
B = [[A, 1], [0, 1]]
P = mat_pow(B, X, M)
print(P[0][1])
