def count_set_bits(n: int) -> int:
  count = 0
  while n:
    n &= n-1
    count += 1

  return count

N = int(input())
tlg = [] # testimony list group
for _ in range(N):
  A = int(input())
  tl = []
  for _ in range(A):
    x, y = (int(x) for x in input().split())
    tl.append((x-1,y))

  tlg.append(tl)

max_val = 0
for p in range(1 << N):
  ok = True
  for i in range(N):
    type = (p >> i) & 1
    if type == 0:
      continue

    if any(((p >> x) & 1) != y for x, y in tlg[i]):
      ok = False
      break

  if ok:
    max_val = max(max_val, count_set_bits(p))

print(max_val)