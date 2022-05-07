N = int(input())
S = list(input())
T = list(input())

ans = 0
j = 1
for i in range(N):
  if S[i] == T[i]:
    continue

  while j < N and S[j] != "1":
    j += 1

  if j == N:
    print(-1)
    exit()

  if S[i] == "0":
    S[i], S[j] = S[j], S[i]
  else:
    S[i] = S[i+1] = S[j] = "0"

  ans += j - i

print(ans)