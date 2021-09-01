N, M = (int(x) for x in input().split())
lines = []
for _ in range(M):
  L, R = (int(x) for x in input().split())
  lines.append((L, R))

cnt = 0
for i in range(M):
  for j in range(i+1, M):
    if lines[i][0] < lines[j][0] and lines[j][0] < lines[i][1] and lines[i][1] < lines[j][1]:
      cnt += 1

    if lines[j][0] < lines[i][0] and lines[i][0] < lines[j][1] and lines[j][1] < lines[i][1]:
      cnt += 1

print(cnt)

