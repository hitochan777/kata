
def sieve(n):
  sieve = [True] * (n + 1)
  primes = []
  for i in range(2, n + 1):
      if sieve[i]:
        primes.append(i)
        for j in range(i, n + 1, i):
            sieve[j] = False

  return primes

N = int(input())
cnt = 0
primes = sieve(10**6)
for i in range(len(primes)):
  for j in range(i+1, len(primes)):
    if primes[i] * (primes[j]**3) > N:
      break

    cnt += 1

print(cnt)