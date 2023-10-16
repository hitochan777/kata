S = input()

def is_palindrome(s: str) -> bool:
  return all(s[i] == s[len(s)-i-1] for i in range(len(s) >> 1))

if is_palindrome(S):
  print("Yes")
  exit()

ep = len(S) - 1
while ep >= 0 and S[ep] == "a":
  ep -= 1

sp = 0 
while sp < len(S) and S[sp] == "a":
  sp += 1

if sp <= len(S) - (ep + 1) and is_palindrome(S[sp:ep+1]):
  print("Yes")
else:
  print("No")