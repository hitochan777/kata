N, K = (int(x) for x in input().split())
strs = []
for _ in range(N):
  S = input()
  strs.append(S)

max_val = 0
for i in range(1 << N):
  val = 0
  for j in range(ord("a"), ord("z")+1):
    cnt = 0
    c = chr(j)
    b = i
    for k in range(N):
      if (b >> k) & 1 == 1:
        if c in strs[k]:
          cnt += 1

    if cnt == K:
      val += 1

  max_val = max(max_val, val)

print(max_val)
  