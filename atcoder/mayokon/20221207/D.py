S = input()
T = input()

m = {}
m2 = {}
for s, t in zip(S,T):
  if t in m and m[t] != s:
    print("No")
    exit()

  if s in m2 and m2[s] != t:
    print("No")
    exit()

  m[t] = s
  m2[s] = t

print("Yes")
