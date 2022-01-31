import math
N = int(input())
for _ in range(N):
  hc, dc = (int(x) for x in input().split())
  hm, dm = (int(x) for x in input().split())
  k, w, a = (int(x) for x in input().split())
  ok = False
  for ca in range(k+1):
    H = hc + a * ca
    D = dc + w * (k - ca)
    if math.ceil(hm / D) <= math.ceil(H / dm):
      ok = True
      break

  if ok:
    print("YES")
  else:
    print("NO")