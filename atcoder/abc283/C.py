S = input()[::-1]
ans = 0
i = 0
while i < len(S):
  if S[i] != "0":
    ans += 1
    i += 1
  else:
    if i < len(S)-1 and S[i+1] == "0":
      i += 2
      ans += 1
    else:
      i += 1
      ans += 1

print(ans)

