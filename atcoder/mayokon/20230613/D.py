from itertools import permutations
from collections import defaultdict

H, W = (int(x) for x in input().split())
C = []
for _ in range(10):
  c = list(int(x) for x in input().split())
  C.append(c)

cnt = defaultdict(int)
for _ in range(H):
  A = (int(x) for x in input().split())
  for a in A:
    cnt[a] += 1

magics = defaultdict(lambda: 10**18)
li = [0, 2, 3, 4, 5, 6, 7, 8, 9]
for ps in permutations(li):
  ar = list(ps) + [1]
  acc = [0]
  for i in range(8, -1, -1):
    acc.append(C[ar[i]][ar[i+1]] + acc[-1])

  for num, magic in zip(ar, acc[::-1]):
    magics[num] = min(magics[num], magic)

ans = 0
for i in range(10):
  ans += cnt[i] * magics[i]

print(ans)