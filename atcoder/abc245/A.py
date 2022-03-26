# N = int(input())
A, B, C, D = (int(x) for x in input().split())
if A * 3600 + B * 60 < C * 3600 + D * 60 + 1:
  print("Takahashi")
else:
  print("Aoki")
