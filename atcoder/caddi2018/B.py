N = int(input())
ok = True
for _ in range(N):
  a = int(input())
  if a % 2 == 1:
    ok = False

if ok:
  print("second")
else:
  print("first")