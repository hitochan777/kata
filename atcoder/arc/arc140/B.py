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

print(min(len(cnts) * 2, sum(cnts)))