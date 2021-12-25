from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())
cnt = defaultdict(int)
total = 0
for i in range(N):
  total += cnt[i-A[i]]
  cnt[A[i] + i] += 1

print(total)
