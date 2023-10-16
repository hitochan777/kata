S = input()
used = set()
A = []
for c in S:
  if c == "(":
    alp = set()
    A.append("(")
  elif c == ")":
    while True:
      c2 = A.pop()
      if c2 == "(":
        break

      used.remove(c2)
  else:
    if c in used:
      print("No")
      exit()
    else:
      used.add(c)
      A.append(c)

print("Yes")


# b(a)ba