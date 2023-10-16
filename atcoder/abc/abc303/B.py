N, M = (int(x) for x in input().split())
ok = set()
for _ in range(M):
  A = list(int(x) for x in input().split())
  for i in range(N-1):
    ok.add((min(A[i], A[i+1]), max(A[i+1], A[i])))

print(N * (N-1) // 2 - len(ok))