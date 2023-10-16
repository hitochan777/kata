N = int(input())
S = list(int(x) for x in input().split())
A = []
for i in range(N-1,0,-1):
  A.append(S[i] - S[i-1])

A.append(S[0])

print(*A[::-1])
