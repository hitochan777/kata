N, M = (int(x) for x in input().split())
S = []
for _ in range(N):
  S.append(input())

cnt = 0
for i in range(N):
  for j in range(i+1,N):
    A = S[i]
    B = S[j]
    if all(A[m] == "o" or B[m] == "o" for m in range(M)):
      cnt += 1

print(cnt)
