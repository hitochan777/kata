from base64 import b32decode
from locale import ABDAY_3


N = int(input())
A = list(int(x) for x in input().split())

B = [0] * (N + 1)

for i in range(N, 0, -1):
  rem = sum(B[j] for j in range(i*2, N+1,i))
  B[i] = (A[i-1] + rem) % 2

bs = [i+1 for i, b in enumerate(B[1:]) if b == 1]
print(len(bs))
print(*bs)