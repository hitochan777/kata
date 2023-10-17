def is_palindrome(S):
  N = len(S)
  return all(S[i] == S[N-i-1] for i in range(N//2))


S = input()
ans = 0
for i in range(len(S)):
  for j in range(i, len(S)):
    if is_palindrome(S[i:j+1]):
      # print(S[i:j+1])
      ans = max(ans, j-i+1)


print(ans)