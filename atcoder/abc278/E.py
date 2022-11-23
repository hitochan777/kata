from collections import defaultdict
import sys
H, W, N, h, w = (int(x) for x in input().split())
# cnt = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
cnt = [[[0 for _ in range(N + 1)] for _ in range(W + 1)] for _ in range(H + 1)]

A = []
for i in range(H):
  a = list(int(x) for x in sys.stdin.readline().split())
  A.append(a)

for i in range(1,H+1):
  for j in range(1,W+1):
    cnt[i][j][A[i-1][j-1]] = 1

# print("joge")

for i in range(1,H+1):
  for j in range(1,W+1):
    for k in range(1,N+1):
      cnt[i][j][k] += cnt[i][j-1][k]

for j in range(1,W+1):
  for i in range(1,H+1):
    for k in range(1,N+1):
      cnt[i][j][k] += cnt[i-1][j][k]

# print("done")
for i in range(1, H-h+2):
  row = []
  for j in range(1, W-w+2):
    total = N
    for k in range(1,N+1):
      tmp = cnt[i+h-1][j+w-1][k] - cnt[i+h-1][j-1][k] - cnt[i-1][j+w-1][k] + cnt[i-1][j-1][k]
      if cnt[H][W][k] - tmp == 0:
        total -= 1

    row.append(total)

  print(*row)
