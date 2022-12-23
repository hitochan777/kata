from collections import defaultdict
N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
acc = [0]
for a in A:
  acc.append(acc[-1]+a)

cnt = defaultdict(int)
ans = 0
for i in range(N, -1, -1):
  ans += cnt[acc[i] + K]
  cnt[acc[i]] += 1

print(ans)