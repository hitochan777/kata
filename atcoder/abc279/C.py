H, W = (int(x) for x in input().split())
S = [[] for _ in range(W)]
T = [[] for _ in range(W)]
for _ in range(H):
  row = input()
  for i, c in enumerate(row):
    S[i].append(c)

for i in range(W):
  S[i] = "".join(S[i])

for _ in range(H):
  row = input()
  for i, c in enumerate(row):
    T[i].append(c) 

for i in range(W):
  T[i] = "".join(T[i])

S.sort()
T.sort()
if all(s == t for s, t in zip(S, T)):
  print("Yes")
else:
  print("No")