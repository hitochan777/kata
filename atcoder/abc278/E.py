from collections import defaultdict
H, W, N, h, w = (int(x) for x in input().split())
cnt = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

A = []
for i in range(H):
  a = list(int(x) for x in input().split())
  A.append(a)

for i in range(H):
  for j in range(W):
    for k, v in cnt[i][j-1].items():
      cnt[i][j][k] += v

    cnt[i][j][A[i][j]] += 1

for j in range(W):
  for i in range(H):
    for k, v in cnt[i-1][j].items():
      cnt[i][j][k] += v

for i in range(0, H-h+1):
  row = []
  for j in range(0, W-w+1):
    total = N
    for k in range(1,N+1):
      tmp = cnt[i+h-1][j+w-1][k] - cnt[i+h-1][j-1][k] - cnt[i-1][j+w-1][k] + cnt[i-1][j-1][k]
      if cnt[H-1][W-1][k] - tmp == 0:
        total -= 1

    row.append(total)

  print(*row)
