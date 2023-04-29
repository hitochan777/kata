N = int(input())

def sieve(num):
  prime = [True for _ in range(num+1)]
  p = 2
  while (p * p <= num):
    if prime[p]:
      for i in range(p * p, num+1, p):
        prime[i] = False

    p += 1
 
  return [p for p in range(2, num+1) if prime[p]]

primes = sieve(10**6)

ans = 0
for i in range(len(primes)): # 53
  if primes[i]**5 >= N:
    break

  val1 = primes[i]**2
  for j in range(i+1, len(primes)): # 75000
    if val1 * primes[j]**3 >= N:
      break

    val2 = val1 * primes[j]
    for k in range(j+1, len(primes)):
      val3 = val2 * primes[k]**2
      if val3 > N:
        break

      # print(primes[i], primes[j], primes[k])
      ans += 1

print(ans)
