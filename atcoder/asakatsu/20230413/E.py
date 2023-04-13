N = int(input())
def solve(l, r, deep=False):
  if l > r:
    return 0
  
  if len(str(r)) == len(str(l)):
    return r - l + 1

  N = len(str(r))
  ret = r % (10**(N-1)) + 1
  diff = ((r // (10**(N-1))) - 1) * 10**(N-1)
  ret += diff
  if diff > 0 and deep:
    ret += -1
  
  ret += solve(max(l, r % (10**(N-1))+1), 10**(N-1)-1, True)
  # print(l, r, ret)
  return ret
for _ in range(N):
  l, r = (int(x) for x in input().split())
  print(solve(l, r))
