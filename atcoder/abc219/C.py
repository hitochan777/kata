X = input()
d = {}
for i, x in enumerate(X):
  d[x] = i

N = int(input())
names = []
for _ in range(N):
  S = input()
  T = "".join(chr(ord('a') + d[c]) for c in S)
  names.append((T, S))

names.sort()

for _, s in names:
  print(s)