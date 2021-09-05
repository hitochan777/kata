from typing import List

class Compressor:
  def __init__(self, li: List[int]):
    self._dedpued_list = sorted(list(set(li)))
    self._d = {v: (i+1) for i, v in enumerate(self._dedpued_list)}

  def get_original(self, n: int) -> int:
    return self._dedpued_list[n-1]

  def compress(self, n: int) -> int:
    return self._d[n]

  def size(self) -> int:
    return len(self._dedpued_list)


class Bit:
  def __init__(self, n):
    self.size = n
    self.tree = [0] * (n + 1)
    self.depth = n.bit_length()

  def sum(self, i):
    s = 0
    while i > 0:
      s += self.tree[i]
      i -= i & -i

    return s
 
  def add(self, i, x):
    while i <= self.size:
      self.tree[i] += x
      i += i & -i
 
  def lower_bound(self, x):
    sum_ = 0
    pos = 0
    for i in range(self.depth, -1, -1):
      k = pos + (1 << i)
      if k <= self.size and sum_ + self.tree[k] < x:
        sum_ += self.tree[k]
        pos += 1 << i

    return pos + 1, sum_

L, Q = (int(x) for x in input().split())

queries = []
points = [1, L+1]
for _ in range(Q):
  c, x = (int(x) for x in input().split())
  points.append(x)
  queries.append((c,x))

compressor = Compressor(points)
bit = Bit(compressor.size())
# bit.add(compressor.compress(1), 1)
bit.add(compressor.compress(L), 1)

for c, x in queries:
  idx = compressor.get_original(x)
  if c == 1:
    bit.add(idx, 1)
  else:
    l, _ = bit.lower_bound(bit.sum(idx))
    print(idx, bit.sum(idx), l)
    print(compressor.get_original(l+1) - compressor.get_original(l))