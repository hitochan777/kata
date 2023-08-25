from collections import defaultdict
N, M = (int(x) for x in input().split())
H = list(int(x) for x in input().split())
nbs = defaultdict(set)
for _ in range(M):
  A, B = (int(x)-1 for x in input().split())
  nbs[A].add(B)
  nbs[B].add(A)

ans = 0
for n in range(N):
  nb = nbs[n]
  if all(H[n] > H[m] for m in nb):
    ans += 1

print(ans)