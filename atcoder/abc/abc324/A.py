N = int(input())
A = set(list(int(x) for x in input().split()))
if len(A) == 1:
  print("Yes")
else:
  print("No")