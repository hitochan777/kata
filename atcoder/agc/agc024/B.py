from bisect import bisect_left

def get_lis(A):
  lis = [0] * (len(A) + 1)
  for a in A:
    lis[a] = lis[a-1] + 1

  return max(lis)

N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

lis = get_lis(A)
print(N - lis)