N, X = (int(x) for x in input().split())
S = input()
newS = []
cnt = 0
for i in range(N-1, -1, -1):
  if S[i] == "U":
    cnt += 1
  elif cnt > 0:
    cnt -= 1
  else:
    newS.append(S[i])

newS.extend(["U"] * cnt)
S = newS[::-1]

for s in S:
  if s == "U":
    X //=  2
  elif s == "L":
    X *= 2
  else:
    X = X * 2 + 1

print(X)