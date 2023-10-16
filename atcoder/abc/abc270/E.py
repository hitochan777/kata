N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

ng, ok = -1, K
while ok - ng > 1:
  m = (ok + ng) >> 1
  total = sum(min(m, a) for a in A)
  if total == K:
    ok = m
    break
  elif total > K:
    ok = m
  else:
    ng = m

if total == K:
  print(*[a-min(ok, a) for a in A])
  exit()

total = sum([min(ok-1, a) for a in A])
rem = [a-min(ok-1, a) for a in A]
i = 0
while total < K:
  while rem[i] == 0:
    i += 1

  rem[i] -= 1
  total += 1
  i += 1

print(*rem)




