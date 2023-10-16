N, M = (int(x) for x in input().split())
S = []
for _ in range(N):
    S.append(input())

T = []
for _ in range(M):
  T.append(input())

cnt = 0
for s in S:
  if any(s.endswith(t) for t in T):
    cnt += 1

print(cnt)
      