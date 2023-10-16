from math import gcd

n = int(input())
A = list(map(int, input().split()))

L = [0] * n
R = [0] * n
L[0], R[-1] = A[0], A[-1]

for i in range(1, n):
    L[i] = gcd(L[i-1], A[i])

L = [0] + L

for i in range(n-2, -1, -1):
    R[i] = gcd(R[i+1], A[i])

R = R + [0]

maxGcd = 0
for i in range(n):
    g = gcd(L[i] if L[i] != 0 else R[i+1], R[i+1] if R[i+1] != 0 else L[i])
    maxGcd = max(maxGcd, g)

print(maxGcd)
