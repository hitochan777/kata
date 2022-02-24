N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
cur = sum(A[:K])
total = cur
for i in range(N-K):
  cur += - A[i] + A[i+K] 
  total += cur 

print(total)