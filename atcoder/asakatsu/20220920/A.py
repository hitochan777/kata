N, M, X = (int(x) for x in input().split())
A = set(int(x) for x in input().split())

i = 0
ca, cb = 0, 0,
while i < X:
  if i in A:
    ca += 1

  i += 1

while i < N:
  if i in A:
    cb += 1

  i += 1

print(min(ca, cb))
