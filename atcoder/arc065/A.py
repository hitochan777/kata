strs = ["dream"[::-1], "dreamer"[::-1], "erase"[::-1], "eraser"[::-1]]
def is_possible(S):
  S = S[::-1]
  p = 0
  while p < len(S):
    for s in strs:
      if p + len(s) > len(S):
        continue

      if all(s[i] == S[p+i] for i in range(len(s))):
        p += len(s)
        break
    else:
      return False

  return True


S = input()
print("YES" if is_possible(S) else "NO")
