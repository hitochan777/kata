from collections import defaultdict
N = int(input())
1 * 2 * 3
2 * 3
MOD = 10**9 + 7

def get_divisors_cnt(n: int):
  i = 2
  cnt = defaultdict(int)
  while i**2 <= n:
    while n % i == 0:
      cnt[i] += 1
      n //= i
    
    i += 1

  if n != 1:
    cnt[n] += 1

  return cnt

ans = 0
cnt = defaultdict(int)
for i in range(1, N+1):
  for k, v  in get_divisors_cnt(i).items():
    cnt[k] += v

ans = 1
for v in cnt.values():
  ans *= (v + 1)
  ans %= MOD

print(ans)