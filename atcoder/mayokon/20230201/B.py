from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())
cnt = defaultdict(int)
for a in A:
  cnt[a] += 1 

for i in range(1, N+1):
  print(cnt[i])