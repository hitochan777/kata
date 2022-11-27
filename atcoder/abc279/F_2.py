N, Q = (int(x) for x in input().split())
boxes = [set([i]) for i in range(N)]
num = N

for _ in range(Q):
  q = list(int(x) for x in input().split())
  cmd = q[0]
  if cmd == 1:
    x, y = q[1]-1, q[2]-1
    boxes[x] = boxes[x].union(boxes[y])
    boxes[y] = set()
  elif cmd == 2:
    x = q[1]-1
    boxes[x].add(num)
    num += 1
  else:
    x = q[1]-1
    for i in range(N):
      if x in boxes[i]:
        print(i+1)
        break