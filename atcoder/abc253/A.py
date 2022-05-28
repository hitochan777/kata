A, B, C = (int(x) for x in input().split())
li = sorted([A, B, C])
if li[1] == B:
  print("Yes")
else:
  print("No")
