import math
N, H = (int(x) for x in input().split())
vals = []
for _ in range(N):
    a, b = (int(x) for x in input().split())
    vals.append((a,0))
    vals.append((b,1))

vals.sort(reverse=True)
ans = 0
i = 0
while H > 0:
  x, t = vals[i]
  if t == 0:
    ans += math.ceil(H / x)
    break
  else:
    H -= x
    ans += 1

  i += 1

print(ans)
