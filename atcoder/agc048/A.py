def solve(s: str) -> int:
  idx = None
  for i, c in enumerate(s):
    if c != "a":
      idx = i
      break

  if idx is None:
    return -1

  if s[idx] > "t":
    return idx - 1

  return idx

T = int(input())
for _ in range(T):
  S = input()
  ans = solve(S)
  print(ans)