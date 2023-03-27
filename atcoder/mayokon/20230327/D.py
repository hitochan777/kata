K = int(input())

used = set()
prev = 0
for i in range(K):
  cur = (prev * 10 + 7) % K
  if cur == 0:
    print(i+1)
    exit()

  if cur in used:
    print(-1)
    exit()

  used.add(cur)
  prev = cur

print(-1)