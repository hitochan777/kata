from collections import deque

q = deque()
N = int(input())
A = list(int(x) for x in input().split())
for a in A:
  if len(q) == 0:
    q.append((a,1))
  else:
    top = q.pop()
    if top[0] == a:
      if top[1] == a-1:
        for _ in range(a-2):
          q.pop()
      else:
        q.append(top)
        q.append((a,top[1]+1))

    else:
      q.append(top)
      q.append((a, 1))

  print(len(q))
