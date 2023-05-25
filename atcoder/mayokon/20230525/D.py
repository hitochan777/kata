N = int(input())
A = list(int(x) for x in input().split())
A.sort()
i = 0
while i < N-1:
  B = -A[i]-A[i+1]
  if B <= A[i] + A[i+1]:
    break

  A[i] *= -1
  A[i+1] *= -1

  i += 2

print(sum(A))