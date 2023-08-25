N = int(input())
A = list(int(x) for x in input().split())
ans = 1 << 32
for i in range(1<<N):
  ps = []
  xored = 0
  for j in range(N):
    if (i >> j) & 1 == 0:
      if len(ps) > 0:
        ored = 0
        for num in ps:
          ored |= num

        ps = [] 
        xored ^= ored

    ps.append(A[j])

  if len(ps) > 0:
    ored = 0
    for num in ps:
      ored |= num

    ps = [] 
    xored ^= ored
  
  ans = min(ans, xored)

print(ans)