from collections import defaultdict
N, M = (int(x) for x in input().split())
C = list(x for x in input().split())
D = list(x for x in input().split())
P = list(int(x) for x in input().split())
prices = defaultdict(lambda: P[0])
for d, p in zip(D, P[1:]):
  prices[d] = p

print(sum(prices[c] for c in C))
