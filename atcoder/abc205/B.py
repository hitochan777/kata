N = int(input())
A = list(int(x) for x in input().split())
A.sort()
ok = True 
for i, val in enumerate(A):
  if i + 1 != val:
    ok = False
    break

if ok:
  print("Yes")
else:
  print("No")
  