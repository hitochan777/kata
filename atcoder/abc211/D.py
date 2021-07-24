from collections import defaultdict
import queue

g = defaultdict(list)
N, M = (int(x) for x in input().split())
for _ in range(M):
  A, B = (int(x) for x in input().split())
  g[A].append(B)
  g[B].append(A)

# print(g)

q = queue.Queue()
q.put((1, 0))

dist_dict = defaultdict(lambda: 10**18)
comb_dict = defaultdict(int)
dist_dict[1] = 0
comb_dict[1] = 1
MOD = 10**9 + 7

max_size = 0
while not q.empty() > 0:
  max_size = max(q.qsize(), max_size)
  v = q.get()
  node, d = v[0], v[1]
  for ne in g[node]:
    if d + 1 > dist_dict[ne]:
      continue

    # print(node, ne, comb_dict[ne], comb)
    comb_dict[ne] = (comb_dict[ne] + comb_dict[node]) % MOD
    if dist_dict[ne] == d + 1:
      continue

    dist_dict[ne] = d + 1
    
    q.put((ne, d + 1))

# print(max_size)
print(comb_dict[N])