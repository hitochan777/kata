def solve(a, s):
  if s < 2 * a:
    return False

  return (s - 2 * a) & a == 0


T = int(input())
for _ in range(T):
  a, s = list(int(x) for x in input().split())
  ok = solve(a, s)
  if ok:
    print("Yes")
  else:
    print("No")