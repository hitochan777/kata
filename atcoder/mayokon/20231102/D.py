def SieveOfEratosthenes(num):
  prime = [True for i in range(num+1)]
  p = 2
  while (p * p <= num):
    if prime[p]:
      for i in range(p * p, num+1, p):
        prime[i] = False

    p += 1

  for p in range(2, num+1):
    if prime[p]:
      yield p

N = int(input())
primes = list(SieveOfEratosthenes(10**6))
n = len(primes)

cnt = 0
for i in range(n):
  if primes[i] ** 2 >= N:
    break

  for j in range(i+2, n):
    if (primes[i] ** 2) * (primes[j] ** 2) >= N:
      break

    for k in range(i+1, j):
      if (primes[i] ** 2) * primes[k] * (primes[j] ** 2) > N:
        break

      cnt += 1

print(cnt)