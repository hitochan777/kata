H, W, D = (int(x) for x in input().split())
A = []
pos = {}
for i in range(H):
  a = list(int(x)-1 for x in input().split())
  for j, val in enumerate(a):
    pos[val] = (i, j)

d = {}

def dist(p1, p2):
  return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

for i in range(D):
  d[i] = [0]
  for j in range(i+D, H*W, D):
    p1 = pos[j-D]
    p2 = pos[j]
    d[i].append(d[i][-1] + dist(p1,p2))

# print(d)

Q = int(input())
for _ in range(Q):
  L, R = (int(x)-1 for x in input().split())
  ans = d[R%D][R//D] - d[L%D][L//D]
  print(ans)

