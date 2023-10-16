N = int(input())
def solve(n):
  if n == 1:
    return 3.5

  if n == 2:
    return 4.25

  if n == 3 or n == 4 or n == 5:
    return 2 / 6 * 5.5 + 2 / 3 * solve(n-1)

  return 1 + 5 / 6 * solve(n-1)

print(solve(N))
