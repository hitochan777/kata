from collections import defaultdict

N = int(input())
x_dict = defaultdict(set)
y_dict = defaultdict(set)
xy_set = set()
for _ in range(N):
  x, y = (int(x) for x in input().split())
  x_dict[x].add(y)
  y_dict[y].add(x)
  xy_set.add((x,y))

ans = set()
for x, y in xy_set:
  for y2 in x_dict[x]:
    if y == y2:
      continue

    for x2 in y_dict[y]:
      if x == x2:
        continue

      if ((x2, y2)) in xy_set:
        xs = [x, x2]
        xs.sort()
        ys = [y, y2]
        ys.sort()
        ans.add((xs[0], xs[1], ys[0], ys[1]))

print(len(ans))
