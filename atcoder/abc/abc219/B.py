S1 = input()
S2 = input()
S3 = input()
S = [S1, S2, S3]
T = input()

ans = []
for t in T:
  ans.append(S[int(t) - 1])

print("".join(ans))

