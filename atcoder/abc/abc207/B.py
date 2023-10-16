import math
A, B, C, D = list(int(x) for x in input().split())

deno = C * D - B
if deno <= 0:
  print("-1")
else:
  print(math.ceil(A / deno))