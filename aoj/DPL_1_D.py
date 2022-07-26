from bisect import bisect_left

N = int(input())
A = []
for _ in range(N):
  a = int(input())
  A.append(a)

smallest = [10**18] * N 
for i in range(N):
  idx = bisect_left(smallest, A[i])
  smallest[idx] = min(A[i], smallest[idx])

print(max(i+1 for i in range(N) if smallest[i] < 10**18))
