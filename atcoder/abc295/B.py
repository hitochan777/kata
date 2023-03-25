R, C = (int(x) for x in input().split())
g = []
for _ in range(R):
  g.append(input())

bombed = set()
for i in range(R):
  for j in range(C):
    if g[i][j].isdigit():
      p = int(g[i][j])
      for k in range(max(0, i-p), min(i+p+1, R)):
        for l in range(max(0, j-p), min(j+p+1, C)):
          if abs(i-k) + abs(j-l) <= p:
            bombed.add((k, l))

for i in range(R):
  r = []
  for j in range(C):
    if (i, j) in bombed:
      r.append(".")
    else:
      r.append(g[i][j])

  print("".join(r))