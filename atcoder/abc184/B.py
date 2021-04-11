from collections import Counter

N, X = (int(x) for x in input().split())
S = input()

score = X
for s in S:
  if s == "x":
    score = max(0, score - 1)
  else:
    score += 1

print(score)

