A, B, C = sorted(list(int(x) for x in input().split()))
if A + B < C:
  print(-1)
  exit()
  
print(C)

