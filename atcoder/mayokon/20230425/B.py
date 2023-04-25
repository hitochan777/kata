from collections import Counter
def solve(S: str):
  if S[0] != "A":
    return False
    
  if Counter(S[2:-1])["C"] != 1:
    return False

  idx = S[2:-1].index("C")
  idx += 2
  return (S[1:idx] + S[idx+1:]).islower()

if solve(input()):
  print("AC")
else:
  print("WA")