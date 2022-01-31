from collections import defaultdict
N = int(input())
for _ in range(N):
  cnt = defaultdict(int)
  S = input()
  max_val = 0
  for c in S:
    cnt[c] += 1
    if cnt["0"] == cnt["1"]:
      continue

    max_val = max(min(cnt["0"], cnt["1"]), max_val)

  print(max_val)