X = input()
m = {}
for i, c in enumerate(X):
  m[c] = chr(i + ord("a"))

N = int(input())
strs = []
for _ in range(N):
  s = input()
  converted = "".join([m[c] for c in s])
  strs.append((converted, s))

strs.sort()
for _, s in strs:
  print(s)
