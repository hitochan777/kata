N, M = (int(x) for x in input().split())
cnts = [0] * (N+1)
for _ in range(M):
  L, R = (int(x)-1 for x in input().split())
  cnts[L] += 1
  cnts[R+1] -= 1

for i in range(N):
  cnts[i+1] += cnts[i]

print(sum(1 for c in cnts if c == M))