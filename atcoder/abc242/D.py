import math
def solve(S: str, t: int, k: int):
  if t >= 60:
    target = 0
    offset = k - 1
  else:
    target = (k-1) // (2^t)
    offset = (k-1) % (2^t)

  s0 = (ord(S[target]) - ord("a") + (t % 3)) % 3
  ancestor = (s0 - int(math.log2(offset)) + 300000) % 3
  s = "ABC"
  for c in bin(offset)[2:]:
    if c == "1":
      ancestor = (ancestor + 1) % 3

  return s[ancestor]


S = input()
Q = int(input())
for _ in range(Q):
  t, k = (int(x) for x in input().split())
  ans =  solve(S, t, k)
  print(ans)
