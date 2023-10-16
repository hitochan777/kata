N, D, K = (int(x) for x in input().split())

ranges = []
for _ in range(D):
  L, R = (int(x) for x in input().split())
  ranges.append((L, R))

for _ in range(K):
  S, T = (int(x) for x in input().split())
  cur = S
  to_right = True if T - S > 0 else False
  for i, (L, R) in enumerate(ranges):
    if L <= cur <= R:
      if to_right > 0:
        cur = min(R, T)
      else:
        cur = max(L, T)

      if cur == T:
        print(i+1)
        break

