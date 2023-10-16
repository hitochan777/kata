N = int(input())
ok = True
s = set()
for _ in range(N):
  S = input()
  s.add(S)
  if not (S[0] in "HDCS" and S[1] in "A23456789TJQK"):
    ok = False

if ok and len(s) == N:
  print("Yes")
else:
  print("No")