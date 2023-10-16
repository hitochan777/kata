from typing import Match


from collections import defaultdict

front = defaultdict(lambda: None)
rear = defaultdict(lambda: None)
N, Q = (int(x) for x in input().split())
for _ in range(Q):
  x, *params = (int(x) for x in input().split())
  if x == 1:
    x, y = params
    front[y] = x
    rear[x] = y
  elif x == 2:
    x, y = params
    front[y] = None
    rear[x] = None
  else:
    p = params[0]
    while front[p] is not None:
      p = front[p]

    ans = []
    while p is not None:
      ans.append(str(p)) 
      p = rear[p]

    print(len(ans), " ".join(ans))