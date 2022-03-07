N, X = (int(x) for x in input().split())

def f(l, x):
  if l == 0:
    return 1

  if x == 0:
    return 0

  s = 0
  x -= 1
  if x < total[l-1]:
    s += f(l-1, x)
    return s

  x -= total[l-1]
  if x < 1:
    s += 1
    return s

  x -= 1
  if x < total[l-1]:
    s += f(l-1, x)
    return s

  s += patty[l-1]
  return s


total = [0] * (N+1)
total[0] = 0
for i in range(N):
  total[i+1] = total[i] * 2 + 3

patty = [0] * (N+1)
patty[1] = 1
for i in range(1,N):
  patty[i+1] = patty[i] * 2 + 1

print(f(N,X-1))