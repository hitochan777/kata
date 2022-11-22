N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
acc = [0]
for a in A:
  acc.append(acc[-1]+a)

ans = sum(i*a for i, a in enumerate(A[:M],start=1))
prev = ans
for i in range(N-M):
  tmp = prev - (acc[i+M] - acc[i]) + M*A[i+M]
  ans = max(ans, tmp)
  prev = tmp

print(ans)