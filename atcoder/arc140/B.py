N = int(input())
S = input()
i = 1 # finding R at 0 is meaningless so start from 1
cnts = []
while i < len(S):
  if S[i] != "R":
    i += 1 
    continue

  j = 1
  cnt = 0
  while i-j >= 0 and i+j < len(S) and S[i-j] == "A" and S[i+j] == "C":
    cnt += 1
    j += 1

  if cnt > 0:
    cnts.append(cnt)

  i += j

if len(cnts) == 0:
  print(0)
  exit()

cnts.sort(reverse=True)
i, j = 0, len(cnts)-1
ans = 0
while i < j:
  while cnts[i] > 0 and i < j:
    ans += 2
    cnts[i] -= 1
    cnts[j] = 0
    j -= 1

  if cnts[i] == 0:
    i += 1

ans += min(cnts[i], 2)
print(ans)


