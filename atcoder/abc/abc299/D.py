N = int(input())
ng, ok = 1, N
while ok - ng > 1:
  m = (ok + ng) >> 1
  print(f"? {m}", flush=True)
  S = input()
  if S == "0":
    ng = m
  else:
    ok = m

print(f"! {ok-1}", flush=True)