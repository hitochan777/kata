from collections import Counter
N = int(input())
cnt = Counter(int(x) for x in input().split())
ans = 0
for k1, v1 in cnt.items():
  for k2, v2 in cnt.items():
    if k1 == k2:
      continue

    ans += v1 * v2 * (k1-k2)**2

print(ans//2)