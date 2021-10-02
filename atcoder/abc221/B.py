S = input()
T = input()

def is_typo(s, t):
  if s == t:
    return True
  
  n = len(s)

  for i in range(n-1):
    sp = s[:i] + s[i+1] + s[i] + s[i+2:]
    if sp == t:
      return True

  return False

print("Yes" if is_typo(S, T) else "No")
