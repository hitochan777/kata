from collections import deque, defaultdict
a, N = (int(x) for x in input().split())

q = deque()
q.appendleft(1)
min_val = defaultdict(lambda: 10**18)
min_val[1] = 0
visited = set()
visited.add(1)

cnt = 0
while len(q) > 0:
  cnt+=1
  n = q.pop()
  op_cnt = min_val[n] + 1
  if n % 10 != 0:
    nb = (n % 10) * 10**(len(str(n))-1) + n // 10
    if min_val[nb] > op_cnt:
      min_val[nb] = op_cnt
      q.appendleft(nb)

  if min_val[n*a] > op_cnt and len(str(n * a)) <= len(str(N)):
    min_val[n*a] = op_cnt
    q.appendleft(n*a)


if min_val[N] == 10**18:
  print(-1)
else:
  print(min_val[N])