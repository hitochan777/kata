N, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
X -= 1
s = set([X])

while True:
  X = A[X] - 1
  if X in s:
    break

  s.add(X)

print(len(s))
