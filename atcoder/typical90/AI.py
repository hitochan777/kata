from collections import defaultdict
import sys

sys.setrecursionlimit(10**5+10)
N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  g[A].append(B)
  g[B].append(A)

def dfs(node, prev, K, chosen_nodes):
  chosen_node_total = 0
  match_node_total = 0

  if node in chosen_nodes:
    chosen_node_total += 1

  for nb in g[node]:
    if nb == prev:
      continue

    chosen_node_cnt, match_node_cnt = dfs(nb, node, K, chosen_nodes)
    chosen_node_total += chosen_node_cnt
    match_node_total += match_node_cnt

  if 1 <= chosen_node_total <= K-1:
      match_node_total += 1

  return chosen_node_total, match_node_total

Q = int(input())
for _ in range(Q):
  K, *V = (int(x) for x in input().split())
  _, match_node_total = dfs(0, -1, K, set([v-1 for v in V]))
  print(match_node_total)