N, L = (int(x) for x in input().split())
K = int(input())
A = list(int(x) for x in input().split())

def calc_divisible_count(splits, m, l) -> int:
  splits = [0] + splits + [l]
  n = len(splits)
  cur = 0
  cnt = 0
  for i in range(1, n):
    cur += splits[i]  - splits[i-1]
    if cur >= m:
      cur = 0
      cnt += 1

  # print(splits, m, l, cnt)
  return cnt

l, h = 0, L
while l <= h:
  m = (l + h) >> 1
  if calc_divisible_count(A, m, L) >= K + 1:
    l = m + 1
  else:
    h = m - 1

print(h)