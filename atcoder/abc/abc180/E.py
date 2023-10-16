import itertools
import random


def held_karp(dists):
    n = len(dists)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1

    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return opt, list(reversed(path))


def dist(p1, p2):
  return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + max(0, p2[2]-p1[2])

N = int(input())
pos = []
for _ in range(N):
  pos.append(list(int(x) for x in input().split()))

dist_matrix = []
for i in range(N):
  row = []
  for j in range(N):
    row.append(dist(pos[i], pos[j]))

  dist_matrix.append(row)

print(held_karp(dist_matrix)[0])