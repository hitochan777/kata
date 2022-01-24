from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
N = int(input())

def solve(pairs, used):
  if len(pairs) == N:
    xor = 0
    for x, y in pairs:
      xor ^= happy[x][y-x-1]

    return xor

  a, b = None, None
  for i in range(2*N):
    if not used[i]:
      a = i
      used[a] = True
      break

  max_val = 0
  for i in range(2*N):
    if not used[i]:
      b = i
      used[b] = True
      pairs.append((a,b))
      val = solve(pairs, used)
      max_val = max(val, max_val)
      used[b] = False
      pairs.pop()

  used[a] = False

  return max_val

happy = [] 
for i in range(2 * N - 1):
  A = list(int(x) for x in input().split())
  happy.append(A)

print(solve([], defaultdict(bool)))
