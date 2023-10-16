X = input()

def is_next(s1: str, s2: str) -> bool:
  n1 = int(s1)
  n2 = int(s2)
  return (n1 + 1) % 10 == n2 % 10

def is_weak(s: str) -> bool:
  if len(set(list(X))) == 1:
    return True

  return all(is_next(s[i], s[i+1]) for i in range(len(s)-1))

print("Weak" if is_weak(X) else "Strong")

    
