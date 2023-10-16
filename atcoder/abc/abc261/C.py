from collections import defaultdict


N = int(input())
cnt = defaultdict(int)
for _ in range(N):
  S = input()
  if cnt[S] > 0:
    print(f"{S}({cnt[S]})")
  else:
    print(S)

  cnt[S] += 1