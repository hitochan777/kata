def is_palindrome(s):
  return all(s[i] == s[len(s) - i - 1] for i in range(len(s)//2))

t = int(input())
for _ in range(t):
  n, k = (int(x) for x in input().split())
  s = input()
  if k == 0:
    print(1)
    continue

  if is_palindrome(s):
    print(1)
  else:
    print(2)
  