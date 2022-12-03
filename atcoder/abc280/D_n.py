from collections import defaultdict
K = int(input())

def prime_factorize(n):
    cnt = defaultdict(int)
    while n % 2 == 0:
        cnt[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            cnt[f]+=1
            n //= f
        else:
            f += 2
    if n != 1:
        cnt[n] += 1

    return cnt

Kcnt = prime_factorize(K)
prime_cnt = sum(Kcnt.values())
if prime_cnt == 1:
  print(list(Kcnt.keys())[0])
  exit()

Kset = set(Kcnt.keys())
# print(Kcnt)
n = 1
while True:
  # print(n)
  cnt = prime_factorize(n)
  for k in Kset:
    diff = min(Kcnt[k], cnt[k])
    prime_cnt -= diff
    Kcnt[k] -= diff

  if prime_cnt == 0:
    print(n)
    exit()

  n += 1