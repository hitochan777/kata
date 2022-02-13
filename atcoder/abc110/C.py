S = input()
T = input()
m = {}
m2 = {}
for c1, c2 in zip(S, T):
  if c1 not in m:
    m[c1] = c2

  if c2 in m2 and m2[c2] != c1:
    print("No")
    exit()

  m2[c2] = c1

  if m[c1] != c2:
    print("No")
    exit()

print("Yes")