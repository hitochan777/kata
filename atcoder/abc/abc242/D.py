def solve(S, t, k):
  if t == 0:
    return S[k]
  
  if k == 0:
    offset = ((ord(S[0]) - ord("A")) + t) % 3
    return chr(ord("A") + offset)

  return chr(ord("A") + ((ord(solve(S, t-1, k//2)) - ord("A") + k % 2 + 1) % 3))

S = input()
Q = int(input())
for _ in range(Q):
  t, k = (int(x) for x in input().split())
  ans =  solve(S, t, k-1)
  print(ans)
