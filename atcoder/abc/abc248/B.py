A, B, K = (int(x) for x in input().split())
cnt = 0
while A < B:
  A *= K
  cnt += 1

print(cnt)