N = int(input())
S = input()
idx = S.find("ABC")
if idx < 0:
  print(-1)
else:
  print(idx+1)