N = int(input())

def find_min(n: int) -> int:
  if n % 7 == 0:
    return n

  ns = str(n)
  min_cnt = 10
  min_val = None
  for i in range(10,1000):
    if len(str(i)) != len(ns):
      continue

    if i % 7 == 0:
      cnt = sum(1 for c1, c2 in zip(ns, str(i)) if c1 != c2)
      if min_cnt > cnt:
        min_cnt = cnt
        min_val = i

  return min_val


for _ in range(N):
  n = int(input())
  print(find_min(n))
