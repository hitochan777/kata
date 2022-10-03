A, B, C, D = (int(x) for x in input().split())
L = A + B
R = C + D

if L > R:
  print("Left")
elif L == R:
  print("Balanced")
else:
  print("Right")