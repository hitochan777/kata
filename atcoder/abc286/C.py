N, A, B = (int(x) for x in input().split())
S = input()

ans = 10**18
for i in range(N):
  val = A * i
  T = S[i:] + S[:i]
  cnt = sum(1 for j in range(N//2) if T[j] != T[N-j-1])
  val += cnt * B
  ans = min(val, ans)

print(ans)