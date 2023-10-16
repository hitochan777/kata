import math

A, B, K = (int(x) for x in input().split())
N = A + B
ans = ""
for i in range(N):
  a_comb = math.comb(A + B - 1, A - 1) if A > 0 else 0
  b_comb = math.comb(A + B - 1, B - 1) if B > 0 else 0
  if K <= a_comb:
    A -= 1
    ans += "a"
  else:
    K -= a_comb
    B -= 1
    ans += "b"

print(ans)