N = int(input())
ng, ok = 0, N+1
while ok - ng > 1:
  m = (ok + ng) // 2
  print(f"? {ng+1} {m} {1} {N}")
  T = int(input())
  if T == m - ng:
    ng = m
  else:
    ok = m

x = ok
ng, ok = 0, N+1
while ok - ng > 1:
  m = (ok + ng) // 2
  print(f"? {1} {N} {ng+1} {m}")
  T = int(input())
  if T == m - ng:
    ng = m
  else:
    ok = m

y = ok
print(f"! {x} {y}")