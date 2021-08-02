A, B = (int(x) for x in input().split())

if A > 0 and B == 0:
  print("Gold")
elif A == 0 and B > 0:
  print("Silver")
else:
  print("Alloy")