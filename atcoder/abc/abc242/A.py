A, B, C, X = (int(x) for x in input().split())

if X <= A:
  print(1)
elif A + 1 <= X <= B:
  print(min(C/(B - A),1))
else:
  print(0)