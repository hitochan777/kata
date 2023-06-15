from collections import defaultdict

N, M = (int(x) for x in input().split())
prefs = defaultdict(list)
for i in range(M):
  P, Y = (int(x) for x in input().split())
  prefs[P].append((Y, i))

cities = []
for p in prefs.keys():
  prefs[p].sort()
  for i, (_, c) in enumerate(prefs[p], start=1):
    cities.append((c, str(p).zfill(6) + str(i).zfill(6)))

cities.sort()
for _, id in cities:
  print(id)
