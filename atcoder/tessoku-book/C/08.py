N = int(input())
lotteries = []
for _ in range(N):
  S, T = (x for x in input().split())
  T = int(T)
  lotteries.append((S, T))

def get_rank(s, t):
  diff = sum(1 for a, b in zip(s,t) if a != b)
  if diff == 0:
    return 1
  elif diff == 1:
    return 2
  else:
    return 3

ans = None
for i in range(10000):
  s = str(i).zfill(4)
  if not all(get_rank(s,t) == r for t, r in lotteries):
    continue

  if ans is not None:
    print("Can't Solve")
    exit()
  else:
    ans = s

print(ans)

