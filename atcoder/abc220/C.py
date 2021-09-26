N = int(input())
A = list(int(x) for x in input().split())
X = int(input())

total = sum(A)
k = N * (X // total)
rem = X - total * (X // total)
if rem >= 0:
  for i in range(N):
    rem -= A[i]
    k += 1
    if rem < 0:
      break

print(k)