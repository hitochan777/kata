from collections import deque
Q = int(input())
MOD = 998244353
cur = 1
q = deque()
q.appendleft(1)
for _ in range(Q):
  query = list(int(x) for x in input().split())
  if query[0] == 1:
    cur = (cur * 10 + query[1]) % MOD
    q.appendleft(query[1])
  elif query[0] == 2:
    v = q.pop()
    p = pow(10, len(q), MOD)
    cur = (cur + ((MOD - 1) * v * p) % MOD) % MOD
  else:
    print(cur)