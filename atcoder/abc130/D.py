N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

res = N+1
right = 0;
total = 0;
for left in range(N):
  while right < N and total < x:
    sum += A[right]
    right += 1

  if total < K:
    break
  
  res = min(res, right - left)
  if right == left:
    right += 1
  else:
    total -= A[left]
