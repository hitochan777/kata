from collections import Counter
N = int(input())
D = list(int(x) for x in input().split())
M = int(input())
T = list(int(x) for x in input().split())

cnt = Counter(D)
for t in T:
  if cnt[t] > 0:
    cnt[t] -= 1
  else:
    print("NO")
    exit()

print("YES")