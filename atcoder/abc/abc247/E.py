N, X, Y = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def solve(A):
  cnt = 0
  px, py, pz = -1, -1, -1
  for i, a in enumerate(A):
    if a == X:
      px = i
    if a == Y:
      py = i
    if a < Y or a > X:
      pz = i 

    cnt += max(0, min(px, py) - pz)

  return cnt

print(solve(A))