
def solve():
  A, B, C = (int(x) for x in input().split())
  for i in range(C, 1001, C):
    if A <= i <= B:
      return i

  return -1

print(solve())

