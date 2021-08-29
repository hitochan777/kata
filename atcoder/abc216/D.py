from collections import deque

N, M = (int(x) for x in input().split())
q = deque()
cylinders = [deque() for _ in range(M)]
locations = [[] for _ in range(N)]
for i in range(M):
  k = int(input())
  for word in input().split():
    x = int(word) - 1
    cylinders[i].append(x)

  locations[cylinders[i][0]].append(i)

for n in range(N):
  if len(locations[n]) == 2:
    q.append(n)

while len(q) > 0:
  x = q.pop()
  for l in locations[x]:
    cylinders[l].pop()
    if len(cylinders[l]) > 0:
      val = cylinders[l][0]
      locations[val].append(l)
      if len(locations[val]) == 2:
        q.append(val)

is_value_left = any(len(cylinders[i]) > 0 for i in range(M))

print("No" if is_value_left else "Yes")

  