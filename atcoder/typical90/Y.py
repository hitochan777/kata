from functools import reduce

N, B = (int(x) for x in input().split())

def is_same(S: str, T: str) -> bool:
  return sorted(S) == sorted(T)

def mul(S: str) -> int:
  return reduce(lambda a, b: int(a) * int(b), list(S), 1)


def dfs(num: str, nxt: int) -> int:
  # print(num)
  if len(num) > 0 and int(num) > N:
    return 0

  cnt = 0
  if len(num) > 0 and is_same(str(mul(num) + B), num):
    cnt += 1

  for i in range(nxt, 10):
    cnt += dfs(num+chr(ord('0') + i), i)

  return cnt

ans = dfs("", 0)
print(ans)