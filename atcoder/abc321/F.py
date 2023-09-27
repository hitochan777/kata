Q, K = (int(x) for x in input().split())
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(Q+1, K+1)
for _ in range(Q):
  q, n = input().split()
  n = int(n)
  if q == "+":
    pass
  else:
    pass