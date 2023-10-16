is_prime = [True] * (10**5+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, 10**5 + 1):
  if not is_prime[i]:
    continue

  for j in range(i+i, 10**5+1, i):
    is_prime[j] = False

acc = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
  acc[i] = acc[i-1]
  if i % 2 == 1 and is_prime[i] and is_prime[(i+1)//2]:
    acc[i] += 1

Q = int(input())
for _ in range(Q):
  l, r = (int(x) for x in input().split())
  print(acc[r] - acc[l-1])