N, Td = input().split()
N = int(N)

def is_inserted(s, t):
  i, j = 0, 0
  is_inserted = False
  while i < len(s) and j < len(t):
    if s[i] != t[j]:
      if is_inserted:
        return False

      is_inserted = True
      i -= 1

    i += 1
    j += 1

  return True


def ok(s, t):
  if s == t:
    return True

  if len(s) == len(t) - 1:
    return is_inserted(s, t)
  elif len(s) == len(t)+1:
    return is_inserted(t, s)
  elif len(s) == len(t):
    isDiff = False
    for a, b in zip(s, t):
      if a != b:
        if isDiff:
          return False

        isDiff = True

    return True

  return False



ans = []
for i in range(N):
  S = input()
  if ok(S, Td):
    ans.append(i+1)

print(len(ans))
print(*ans)

