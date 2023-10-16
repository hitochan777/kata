import math
N, A, B = (int(x) for x in input().split())

def lcm(a, b):
  return a * b // math.gcd(a, b)

def sum2(a, d, n):
  return n * (2 * a + (n -1) * d) // 2

C = lcm(A, B) 
total = N * (N + 1) // 2
total -= sum2(A, A, N // A)
total -= sum2(B, B, N // B)
total += sum2(C, C, N // C)
print(total)