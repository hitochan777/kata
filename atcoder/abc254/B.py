N = int(input())

ans = []
for i in range(N):
  ans.append([])
  for j in range(i+1):
    if j == 0 or j == i:
      ans[-1].append(1)
    else:
      ans[-1].append(ans[i-1][j-1] + ans[i-1][j])

  print(*ans[-1])

