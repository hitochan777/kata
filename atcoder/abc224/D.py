from collections import defaultdict, deque
M = int(input())
g = defaultdict(list)
for _ in range(M):
  u, v = (int(x) for x in input().split())
  u, v = u-1, v-1
  g[u].append(v)
  g[v].append(u)

p = list(int(x)-1 for x in input().split())
visited = set()

def is_goal(p):
  return all(key == val for key, val in p.items() if key != 8)

def dict_hash(dictionary):
  return sum(10**i * dictionary[i] for i in dictionary)

def gen_next_states(g, p, visited, empty_idx):
  ret = []
  for nb in g[empty_idx]:
    p2 = dict(p)
    p2[empty_idx], p2[nb] = p2[nb], p2[empty_idx]
    hash = dict_hash(p2)
    if hash in visited:
      continue

    ret.append((p2, nb, hash))
  
  return ret

p_dict = {el: i for i, el in enumerate(p)}
empty_idx = None
for i in range(9):
  if i not in p_dict:
    p_dict[i] = -1
    empty_idx = i
    break

q = deque()
q.append(((p_dict, empty_idx, 0, dict_hash(p_dict))))
visited.add(dict_hash(p_dict))

ans = -1
while len(q) > 0:
  state, empty_idx, cnt, hash = q.popleft()
  if is_goal(state):
    ans = cnt
    break

  for nxt, empty_idx, hash in gen_next_states(g, state, visited, empty_idx):
    q.append((nxt, empty_idx, cnt+1, hash))
    visited.add(hash)

print(ans)
