def get_primes(n):
  ok = [True]*(n+1)
  ok[0] = False
  ok[1] = False
  for p in range(2, n+1):
    if not ok[p]:
      continue

    for q in range(p, n+1, p):
      ok[q] = False

  return ok
    

T = int(input())
primes = set(get_primes(10**7))
for _ in range(T):
  N = int(input())
  for n in primes:
    if N % n == 0:
      N // n

