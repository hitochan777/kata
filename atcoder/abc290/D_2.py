T = int(input())
for i in range(T):
  N, D, K = (int(x) for x in input().split())
  marked = set()
  marked.add(0)
  cur = 0
  for _ in range(K-1):
    cur = (cur + D) % N
    while cur in marked:
      cur = (cur + 1) % N

    marked.add(cur)

  print(cur)
