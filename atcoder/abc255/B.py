N, K = (int(x) for x in input().split())
A = list(int(x)-1 for x in input().split())
setA = set(A)
people = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  people.append((X,Y))

maxd = 0 
for i in range(N):
  if i in setA:
    continue

  mind = 10**18
  for j in setA:
    x1, y1 = people[i]
    x2, y2 = people[j]
    d = (x1-x2)**2 + (y1-y2)**2
    mind = min(mind, d)

  maxd = max(mind, maxd)

print(maxd **0.5)

# for i in range(N):
#   for j in range(i+1,N):
#     x1, y1 = people[i]
#     x2, y2 = people[j]
#     d = (x1-x2)**2 + (y1-y2)**2
#     print(i, j, d**0.5)