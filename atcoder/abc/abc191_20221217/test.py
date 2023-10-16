from math import isqrt
import random
for i in range(100000000):
  val = random.randint(0,10**18+1)
  a = isqrt(val)
  b = int(val**0.5)
  assert a == b, f"{a} != {b} when val == {val}"