H, W = (int(x) for x in input().split())
def solve(S):
  for i in range(len(S)-1):
     if S[i] == "T" and S[i+1] == "T":
        S[i], S[i+1] = "P", "C"
      
  return "".join(S)

for _ in range(H):
    S = list(input())
    print(solve(S))