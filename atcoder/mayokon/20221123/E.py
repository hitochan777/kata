from atcoder.segtree import SegTree

INF = 10**18
N, M = (int(x) for x in input().split())
S = input()
st = SegTree(lambda a, b: min(a,b), INF, N+1)
dp = [INF] * (N+1)
dp[0] = 0
st.set(0, 0)
for i in range(1,N+1):
  m = st.prod(max(0,i-M), i) if S[i] == "0" else INF
  if m < INF:
    dp[i] = m+1
    st.set(i, dp[i])

p = N
val = dp[N]
if val == INF:
  print(-1)
  exit()

ans = []
while p != 0:
  for i in range(M, 0, -1):
    if p-i >= 0 and dp[p-i] == val-1:
      ans.append(i)
      p -= i
      val-=1
      break
  
print(*ans[::-1])
