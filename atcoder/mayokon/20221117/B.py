def solve(N, M, prev):
  if N == 0:
    return [[]]

  ans = []
  for i in range(prev+1, M+1):
    for li in solve(N-1, M, i):
      ans.append([i] + li)

  return ans

N, M = (int(x) for x in input().split())
for li in solve(N, M, 0):
  print(*li)