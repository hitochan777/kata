import bisect
L, N1, N2 = (int(x) for x in input().split())
vals1 = []
acc1 = [0]
seps_set = set()
seps_set.add(0)
for _ in range(N1):
  v, l = (int(x) for x in input().split())
  vals1.append(v)
  x = acc1[-1] + l
  acc1.append(x)
  seps_set.add(x)

vals2 = []
acc2 = [0]
for _ in range(N2):
  v, l = (int(x) for x in input().split())
  vals2.append(v)
  x = acc2[-1] + l
  acc2.append(x)
  seps_set.add(x)

seps = sorted(list(seps_set))
# print(seps)
# print(acc1, vals1)
# print(acc2, vals2)

ans = 0
for i in range(1, len(seps)):
  x = bisect.bisect_left(acc1, seps[i])
  y = bisect.bisect_left(acc2, seps[i])
  # print(i, x, y, vals1[x-1], vals2[y-1], seps[i])
  if vals1[x-1] == vals2[y-1]:
    # print("yeah", seps[i] - seps[i-1])
    ans += seps[i] - seps[i-1]

print(ans)
  
