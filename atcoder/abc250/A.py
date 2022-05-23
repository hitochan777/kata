H, W = (int(x) for x in input().split())
R, C = (int(x) for x in input().split())
R, C = R-1, C-1

cnt = 0
for i in range(H):
  for j in range(W):
    if abs(i - R) + abs(j - C) == 1:
      cnt += 1

print(cnt)