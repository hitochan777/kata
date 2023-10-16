import math

def get_primes(n):
  ok = [True]*(n+1)
  ok[0] = False
  ok[1] = False
  for p in range(2, n+1):
    if not ok[p]:
      continue

    for q in range(p*2, n+1, p):
      ok[q] = False

  return [i for i in range(n+1) if ok[i]]

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

T = int(input())
primes = set(get_primes(3*10**6+1))
# print(primes)
for _ in range(T):
  N = int(input())
  for n in primes:
    if N % (n**2) == 0:
      print(n, N // (n**2))
      break
    
    if N % n == 0 and is_square(N//n):
      print(math.isqrt(N//n), n)
      break

