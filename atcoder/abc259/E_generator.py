from random import randint

primes = [2,3,5,7,11,13,17,19,23,29]
N = randint(1,10)
print(N)
for _ in range(N):
  m = randint(1,3)
  start = 0
  print(m)
  for _ in range(m):
    idx = randint(start,len(primes)-1)
    p = primes[idx]
    e = randint(1, 3)
    start = idx + 1
    print(p, e)

