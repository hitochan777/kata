from collections import Counter, defaultdict
N = int(input())
cnt = Counter(int(x) for x in input().split())
A = []
e = defaultdict(bool)
dup = set()
for k, v in cnt.items():
  if v > 1:
    dup.add(k)

  A.append(k)

A.sort()
# print(A)

for a in A:
  if e[a]:
    continue

  for i in range(a*2, 10**6+1, a):
    e[i] = True

ans = 0
for a in A:
  if not e[a] and a not in dup:
    # print(a)
    ans += 1

print(ans)