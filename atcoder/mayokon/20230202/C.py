from collections import deque
q = deque()
Q = int(input())
for _ in range(Q):
    cmd, *a = list(int(x) for x in input().split())
    if cmd == 1:
      x, c = a
      q.append((x,c))
    else:
      cnt = a[0]
      total = 0
      while cnt > 0:
        x, c = q.popleft()
        diff = min(cnt, c)
        total += diff * x
        cnt -= diff
        if c > diff:
           q.appendleft((x, c-diff))

      print(total)

