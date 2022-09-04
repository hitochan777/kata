N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

acc = [0]
for a in A:
  acc.append(acc[-1] + a)

ans = sum(A[i] for i in range(M))
prev = ans
for k in range(1,N-M):
  prev = prev - (acc[M+k] - acc[k]) + M * A[M+1+k]
  print(prev)
  ans = max(prev, ans)

print(ans)


