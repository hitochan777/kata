from collections import defaultdict
import re
N = int(input())
d = {}
people = []
for i in range(N):
  x, y = (int(x) for x in input().split())
  people.append((x,y))

S = input()
d = defaultdict(list)
for i, (x, y) in enumerate(people):
  d[y].append((x, S[i]))

for y in d.keys():
  d[y].sort()
  s = "".join([c for _, c in d[y]])
  s = re.sub(r'(\w)(?=\1)', '', s)
  if len(s) > 2:
    print("Yes")
    exit()

  if len(s) == 2:
    if s != "LR":
      print("Yes")
      exit()


print("No")