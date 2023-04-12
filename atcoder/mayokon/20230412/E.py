from bisect import bisect_left

A, B, Q = (int(x) for x in input().split())
S = [-10**18]
for _ in range(A):
  s = int(input())
  S.append(s)
S.append(10**18)

T = [-10**18]
for _ in range(B):
  t = int(input())
  T.append(t)
T.append(10**18)

def solve(x, S, T):
  ans = 10**18
  idx1 = bisect_left(S, x)
  idx2 = bisect_left(T, x)
  ans = min(ans, max(abs(x-S[idx1-1]), abs(x-T[idx2-1])))

  idx1 = bisect_left(S, x)
  idx2 = bisect_left(T, x)
  ans = min(ans, max(abs(x-S[idx1]), abs(x-T[idx2])))

  idx = bisect_left(S, x)
  shrine = min(abs(x-S[idx-1]), abs(x-S[idx]))
  idx = bisect_left(T, x)
  temple = min(abs(x-T[idx-1]), abs(x-T[idx]))
  ans = min(ans, shrine * 2 + temple)
  ans = min(ans, shrine + temple * 2)
  # print(ans)
  return ans

for _ in range(Q):
  x = int(input())
  ans = solve(x, S, T)
  print(ans)