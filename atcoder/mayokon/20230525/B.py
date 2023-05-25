from collections import Counter, defaultdict

N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(int(x)-1 for x in input().split())

cc = Counter(C)
bc = defaultdict(int)
for i, b in enumerate(B):
  bc[b] += cc[i]

print(sum(bc[a] for a in A))
