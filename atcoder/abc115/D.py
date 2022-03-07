N, X = (int(x) for x in input().split())

def f(l, x):
  if l == 0:
    return 1

  if x < 1:
    return 0

  x -= 1
  if x < total[l-1]:
    return f(l-1, x)

  x -= total[l-1]
  if x < 1:
    return patty[l-1] + 1

  x -= 1
  if x < total[l-1]:
    return patty[l-1] + 1 + f(l-1, x)


  return patty[l-1] * 2 + 1 


total = [0] * (N+1)
total[0] = 1
for i in range(N):
  total[i+1] = total[i] * 2 + 3

patty = [0] * (N+1)
patty[0] = 1
for i in range(N):
  patty[i+1] = patty[i] * 2 + 1
  
print(f(N,X-1))