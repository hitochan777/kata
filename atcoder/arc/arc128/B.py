T = int(input())
for _ in range(T):
  ans = 10**18
  A = [int(x) for x in input().split()]
  A.sort()
  for i in range(3):
    for j in range(i+1, 3):
      if A[j] % 3 == A[i] % 3:
        ans = min(ans, A[j])

  if ans == 10**18:
    print(-1)
  else:
    print(ans)


