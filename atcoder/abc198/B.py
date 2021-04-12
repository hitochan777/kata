S = input()

def is_palindrome(s: str) -> bool:
  return s == s[::-1]

def solve(S: str) -> bool:
  for i in range(10):
    if is_palindrome(S):
      return True

    S = "0" + S

  return False

print("Yes" if solve(S) else "No")
