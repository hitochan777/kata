S = input().split()
T = input().split()

diff = sum(1 for s, t in zip(S, T) if s != t)
if diff == 2:
  print("No")
else:
  print("Yes")