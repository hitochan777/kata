from collections import Counter

N = int(input())
A = list(int(x) for x in input().split())

cnt = Counter(A)
ans = 0
for i, a in enumerate(A):
  ans += N - i - cnt[a]
  cnt[a] -= 1

print(ans)
