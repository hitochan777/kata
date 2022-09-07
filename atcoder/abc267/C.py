N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

acc = [0]
for a in A:
  acc.append(acc[-1] + a)

ans = sum((i+1) * A[i] for i in range(M))
prev = ans
for k in range(N-M):
  prev = prev - (acc[M+k] - acc[k]) + M * A[M+k]
  ans = max(prev, ans)

print(ans)


