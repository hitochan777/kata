N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

acc = [0]
for a in A:
  acc.append(acc[-1]+a)

r = 1
ans = 0
for i in range(N):
  if A[i] > K:
    continue

  while r < N and acc[r+1] - acc[i] <= K:
    r += 1

  # print(r-i, r, i)
  ans += r - i
  r -= 1

print(ans)