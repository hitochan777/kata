from collections import defaultdict, deque

M = int(input())
g = defaultdict(list)
for _ in range(M):
  u, v = (int(x) for x in input().split())
  u, v = u-1, v-1
  g[u].append(v)
  g[v].append(u)

s = ["9"] * 9
p = list(int(x) for x in input().split())
for i, el in enumerate(p):
  s[el-1] = f"{i+1}"

visited = set()
q = deque()
q.append((s,0))
visited.add("".join(s))
ans = -1
while len(q) > 0:
  state, cnt = q.popleft()
  if "".join(state) == "123456789":
    ans = cnt
    break

  empty = None
  for i in range(9):
    if state[i] == "9":
      empty = i
      break

  for nb in g[empty]:
    t = state[:]
    t[empty], t[nb] = t[nb], t[empty]
    ts = "".join(t)
    if ts in visited:
      continue

    visited.add(ts)
    q.append((t,cnt+1))

print(ans)