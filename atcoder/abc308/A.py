S = list(int(x) for x in input().split())
if all(100 <= s < 675 and s % 25 == 0 for s in S):
  print("Yes")
else:
  print("No")