N, K = (int(x) for x in input().split())
A = sorted(list(int(x) for x in input().split()))
F = sorted(list(int(x) for x in input().split()), reverse=True)

def achievable(R):
  total = 0
  for a, f in zip(A, F):
    total += max(a - R // f, 0)
    if total > K:
       return False

  return True

ng, ok = -1, 10**18
while ok - ng > 1:
    R = (ok + ng) // 2
    if achievable(R):
        ok = R
    else:
        ng = R

print(ok)
    