from collections import defaultdict, deque

g = defaultdict(list)
N = int(input())
Ts = []
for i in range(N):
    T, K, *A = list(int(x)-1 for x in input().split())
    T += 1
    K += 1
    Ts.append(T)
    for a in A:
      g[i].append(a)

reachable = set()
q = [N-1]
while len(q) > 0:
   node = q.pop()
   reachable.add(node)
   for nb in g[node]:
    if nb not in reachable:
      q.append(nb)

ans = 0
for node in reachable:
  ans += Ts[node]

print(ans)