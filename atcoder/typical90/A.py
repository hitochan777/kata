N, L = (int(x) for x in input().split())
K = int(input())
A = list(int(x) for x in input().split())

def is_divisible(splits, m) -> bool:
  return False

l, h = 0, L
while l < h:
  m = (l + h) >> 2:
  if is_divisible(A, m):
    l = m + 1
  else:
    h = m - 1

print(m)


