def is_palindrome(s):
  N = len(s)
  return all(s[i] == s[N-i-1] for i in range(N//2))

S = input()
N = len(S)
ans = 0
for i in range(N):
  for j in range(i+1, N+1):
    if is_palindrome(S[i:j]):
      ans = max(j-i, ans)

print(ans)