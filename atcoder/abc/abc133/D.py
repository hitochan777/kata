N = int(input())
A = list(int(x) for x in input().split())
A1 = 0
sign = 1
for i in range(N):
  A1 += A[i] * sign
  sign *= -1

ans = [A1]
for i in range(1, N):
  ans.append(2 * A[i-1] - ans[-1])

print(*ans)