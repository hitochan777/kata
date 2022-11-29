S = input()
s = []
for c in S:
  if c in "01":
    s.append(c)
  else:
    if len(s) > 0:
      s.pop()

print("".join(s))