V, T, S, D = (int(x) for x in input().split())

if  V * T <= D <= V * S:
  print("No")
else:
  print("Yes")