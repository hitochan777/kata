from collections import Counter

N, X = (int(x) for x in input().split())
S = input()

cnt = Counter(S)
score = max(0, X - cnt["x"] + cnt["o"])
print(score)

