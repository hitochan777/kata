N, L, R = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

Lmin = [0]
Rmin = [0]
for a in A:
  tmp = min(Lmin[-1] + a, L*len(Lmin))
  Lmin.append(tmp)

for a in A[::-1]:
  tmp = min(Rmin[-1] + a, R*len(Rmin))
  Rmin.append(tmp)

Rmin = Rmin[::-1]

ans = 10**18
for i in range(N+1):
  ans = min(ans, Lmin[i] + Rmin[i])

print(ans)

