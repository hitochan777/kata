N, K = (int(x) for x in input().split())
V = list(int(x) for x in input().split())

ans = 0
for l in range(N+1):
  for r in range(N+1):
    if l + r > min(N, K):
      continue

    minus = []
    plus = []
    for i in range(l):
      if V[i] < 0:
        minus.append(V[i])
      else:
        plus.append(V[i])

    for i in range(r):
      if V[N-i-1] < 0:
        minus.append(V[N-i-1])
      else:
        plus.append(V[N-i-1])

    rem = K - (l + r)
    minus.sort(reverse=True)
    while rem > 0 and len(minus) > 0:
      minus.pop()
      rem -= 1

    total = sum(plus) + sum(minus)
    ans = max(total, ans)

print(ans)