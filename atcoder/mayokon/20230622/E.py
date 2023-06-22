def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

MOD = 998244353
H, W, K = (int(x) for x in input().split())
x1, y1, x2, y2 = (int(x) for x in input().split())
cur = [0] * 4
if (x1, y1) == (x2, y2):
  cur[0] = 1
elif x1 == x2:
  cur[1] = 1
elif y1 == y2:
  cur[2] = 1
else:
  cur[3] = 1

# print(cur)

for k in range(K):
  prev = cur
  cur = [0] * 4
  cur[0] = (prev[1] * 1 + prev[2] * 1) % MOD
  cur[1] = (prev[0] * (W-1) + prev[1] * (W-2) + prev[3] * 1) % MOD
  cur[2] = (prev[0] * (H-1) + prev[2] * (H-2) + prev[3] * 1) % MOD
  cur[3] = (prev[1] * (H-1) + prev[2] * (W-1) + prev[3] * ((W-2) + (H-2))) % MOD
  # print(cur)
  
print(cur[0])