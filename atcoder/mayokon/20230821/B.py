from collections import defaultdict

N = int(input())
cnt = defaultdict(int)
max_cnt = 0
for _ in range(N):
  S = input()
  cnt[S] += 1
  max_cnt = max(cnt[S], max_cnt)

ans = []
for k, v in cnt.items():
  if v == max_cnt:
    ans.append(k)

ans.sort()
for s in ans:
  print(s)
