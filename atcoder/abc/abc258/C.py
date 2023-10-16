N, Q = (int(x) for x in input().split())
S = input()
c = 0
for _ in range(Q):
  t, x = (int(x) for x in input().split())
  if t == 1:
    c = (c - x + N) % N
  else:
    ans = S[(c + x - 1) % N]
    print(ans)