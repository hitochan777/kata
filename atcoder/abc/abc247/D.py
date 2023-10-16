Q = int(input())
balls = []
Cs = []
for _ in range(Q):
  vals = list(int(x) for x in input().split())
  if vals[0] == 1:
    x, c = vals[1], vals[2]
    balls.append((x, c))
  else:
    c = vals[1]
    Cs.append(c)

i = 0
for t in Cs:
  target = t
  total = 0
  while target > 0:
    x, c = balls[i]
    took = min(target, c)
    total += took * x
    c -= took
    target -= took 
    if c == 0:
      i += 1
    else:
      balls[i] = (x, c)

  print(total)