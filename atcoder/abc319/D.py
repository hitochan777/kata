def is_achievable(M, W, Ls):
  cur = 0
  lines = 1
  for L in Ls:
    if L > W:
      return False

    if cur > 0:
      cur += 1

    if cur >= W:
      lines += 1
      cur = 0

    if cur + L <= W:
      cur += L
    else:
      lines += 1
      cur = 0
      cur += L

  # print(lines)
  if lines > M:
      return False

  return True

# print(is_achievable(3, 13, [9,5,2,7,1,8,8,2,1,5,2,3,6]))


N, M = (int(x) for x in input().split())
Ls = list(int(x) for x in input().split())
ng , ok = 0, 10**18
while ok - ng > 1:
  W = (ok + ng) >> 1
  # print(W, ok, ng, is_achievable(M, W, Ls))
  if is_achievable(M, W, Ls):
    ok = W
  else:
    ng = W

print(ok)
  


