from typing import Optional
from atcoder.segtree import SegTree

class MultiSet:
  E = 10**18
  def __init__(self, N) -> None:
    self.N = N
    self.cnt = [0] * N
    self.st = SegTree(lambda a, b: min(a, b), self.E, N)

  def add(self, x: int) -> None:
    self.cnt[x] += 1
    if self.cnt[x] == 1:
      self.st.set(x, x)

  def delete(self, x: int) -> None:
    assert(self.cnt[x] > 0)
    self.cnt[x] -= 1
    if self.cnt[x] == 0:
      self.st.set(x, self.E)

  def lower_bound(self, x: int) -> Optional[int]:
    res = self.st.prod(x, self.N)
    if res == self.E:
      return None

    return res

# coordinate compression + segment tree ??

def get_compress_dict(nums):
  return {v: i for i, v in enumerate(sorted(list(set(nums))))}

N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())
D = list(int(x) for x in input().split())
chocos = list(zip(A, B, [True]*N))
mixed = list(zip(C, D, [False]*M))
mixed.extend(chocos)
x_dict = get_compress_dict(x for x, _, _ in mixed)
y_dict = get_compress_dict(y for _, y, _ in mixed)
for i in range(len(mixed)):
  x, y, is_choco = mixed[i]
  mixed[i] = (x_dict[x], y_dict[y], is_choco)

mixed.sort(reverse=True, key=lambda x: (x[0], x[1]))
ms = MultiSet(N+M)
for x, y, is_choko in mixed:
  if is_choko:
    val = ms.lower_bound(y)
    if val is None:
      print("No")
      exit()

    ms.delete(val)
  else:
    ms.add(y)

print("Yes")