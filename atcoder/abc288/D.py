N, K = (int(x) for x in input().split())
arr = [int(x) for x in input().split()]

def is_good(A, K):
    n = len(A)
    for i in range(n-K+1):
        offset = A[i]
        for j in range(K):
            A[i+j] -= offset

    return all(a == 0 for a in A)

Q = int(input())
for _ in range(Q):
  l, r = (int(x)-1 for x in input().split())
  if is_good(arr[l:r+1], K):
      print("Yes")
  else:
      print("No")
        
# 16 18 33 32 28 26 11 12
# 0  2  17 32 28 26 11 12
# 0  0  15 30 28 26 11 12
# 0  0  0  15 13 26 11 12
# 0  0  0  0  -2 11 11 12
# 0  0  0  0  0  13 13 12
