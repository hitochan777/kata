import sys

def find(parents, x):
  if parents[x] == x:
    return x

  parents[x] = find(parents, parents[x])
  return parents[x]

N = 2**20
values = [-1] * N
parents = list(range(N))
Q = int(input())
for _ in range(Q):
  t, x = (int(x) for x in sys.stdin.readline().split())
  if t == 1:
    l = find(parents, x%N)
    values[l] = x
    parents[l] = find(parents, (l+1)%N)

  else:
    sys.stdout.write(f"{values[x % N]}" + "\n")