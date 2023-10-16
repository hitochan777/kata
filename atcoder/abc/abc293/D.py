from atcoder.dsu import DSU
N, M = (int(x) for x in input().split())


rings = set()
dsu = DSU(N)
for _ in range(M):
  A, B, C, D = (x for x in input().split())
  A = int(A)
  C = int(C)
  A -= 1
  C -= 1
  if dsu.same(A, C):
    rings.add(A)

  dsu.merge(A, C)

new_ring = set()
for ring in rings:
  new_ring.add(dsu.leader(ring))

rings = new_ring
num_rings = 0
num_non_rings = 0
for group in dsu.groups():
  # print(group, dsu.leader(group[0]), rings)
  if dsu.leader(group[0]) in rings:
    num_rings += 1
  else:
    num_non_rings += 1

print(num_rings, num_non_rings)
