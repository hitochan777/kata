N, K = (int(x) for x in input().split())
S = input()
ones = S.count("1")
if ones % 2 == K % 2:
  print("Yes")
else:
  print("No")