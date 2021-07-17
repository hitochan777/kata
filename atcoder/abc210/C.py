from collections import defaultdict, Counter

N, K = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())

cnts = Counter(C[:K])
max_val = len(cnts)
for i in range(1,N-K+1):
  cnts[C[i-1]] -= 1
  if cnts[C[i-1]] == 0:
    del cnts[C[i-1]]

  cnts[C[i+K-1]] += 1
  max_val = max(max_val, len(cnts))

print(max_val)