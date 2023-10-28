N = (int(x) for x in input().split())
R = input()
C = input()

def check(g):
  for i in range(N):
    if g[i][0] != R[i]:
      return False

  for i in range(N):
    if g[0][i] != C[i]:
      return False

  return True

def dfs(g, r ,c):
  if r == N and c == N:
    if check(g):
      print("Yes")
      print(g)
      exit()
  elif r < N:
    for i in range(min(N, 3)):
      g[r][i] = R[r]
      dfs(g, r+1, c)
      g[r][i] = "."
  else:
    idx = None
    for i in range(N):
      if g[i][c] != ".":
        idx = i

    if idx is None:
      for i in range(N):
        g[i][c] = C[c]
        dfs(g, r, c+1)


g = [["."]*N for _ in range(N)]
dfs(g, 0, 0)
print("No")