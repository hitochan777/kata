N = int(input())
S = list(input())
Q = int(input())
is_upper_mode = True
unmatches = set([i for i, c in enumerate(S) if c.islower()])
for _ in range(Q):
  t, x, c = (x for x in input().split())
  t = int(t)
  x = int(x)-1
  if t == 1:
    S[x] = c
    if is_upper_mode:
      if c.islower():
        unmatches.add(x)
      elif x in unmatches:
        unmatches.remove(x)
    else:
      if c.isupper():
        unmatches.add(x)
      elif x in unmatches:
        unmatches.remove(x)

  elif t == 2:
    is_upper_mode = False
    unmatches = set()
  else:
    is_upper_mode = True
    unmatches = set()

res = []
for i, c in enumerate(S):
  if is_upper_mode:
    if i in unmatches:
      converted = c.lower()
    else:
      converted = c.upper()
  else:
    if i in unmatches:
      converted = c.upper()
    else:
      converted = c.lower()

  res.append(converted)
  

print("".join(res))