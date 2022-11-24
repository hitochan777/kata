N = int(input())

def satisfies(S):
  return S[0] in "HDCS" and S[1] in "A23456789TJQK"

Ss = [input() for _ in range(N)]
if all(satisfies(s) for s in Ss) and len(set(Ss)) == N:
  print("Yes")
else:
  print("No")