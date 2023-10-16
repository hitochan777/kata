N = int(input())

def f(a: int, b: int) -> int:
  return (a ** 2 + b ** 2) * (a + b)

min_val = 10**18
for a in range(10**6+1):
  ng, ok = -1, 10**6+1
  while abs(ng - ok) > 1:
    mid = (ok + ng) >> 1
    if f(a, mid) >= N:
      ok = mid
    else:
      ng = mid

  min_val = min(min_val, f(a, ok))

print(min_val)