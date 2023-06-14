import math

def solve(N, S, K):
  visited = set()
  now = S
  ans = 0
  while now not in visited:
    print(now)
    if now == 0:
      return ans

    visited.add(now)
    delta = math.ceil((N - now) / K)
    ans += delta
    now = (now + delta * K) % N

  return -1

T = int(input())
for _ in range(T):
   N, S, K = (int(x) for x in input().split())
   print(solve(N, S, K))