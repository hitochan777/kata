from itertools import groupby

def runLengthEncodeToString(S: str):
    grouped = groupby(S)
    res = [('x', 0)]
    for k, v in grouped:
        res.append((k, len(list(v))))

    res.append(('x', 0))
    return res

N = int(input())
S = input()
S = runLengthEncodeToString(S)
ans = -1
for i in range(1, len(S)):
  if S[i][0] == "o" and "-" in [S[i-1][0], S[i+1][0]]:
    ans = max(ans, S[i][1])

print(ans)