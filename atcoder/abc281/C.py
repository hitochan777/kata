N, T = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
total = sum(A)
T %= total

t = 0
for i,a in enumerate(A):
  duration = T-t
  t += a
  if T <= t:
    print(i+1, duration)
    exit()

