S, T, X = (int(x) for x in input().split())
if S < T:
  print("Yes" if S <= X < T else "No")
else:
  print("No" if T <= X < S else "Yes")