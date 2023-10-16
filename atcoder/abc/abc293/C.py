H, W = (int(x) for x in input().split())

A = []
for _ in range(H):
  row = list(int(x) for x in input().split())
  A.append(row)

def solve(i, j, h, w, nums):
  if i == H-1 and j == W-1:
    return 1

  ans = 0
  if h > 0 and A[i+1][j] not in nums:
    nums.add(A[i+1][j])
    ans += solve(i+1,j,h-1, w, nums)
    nums.remove(A[i+1][j])

  if w > 0 and A[i][j+1] not in nums:
    nums.add(A[i][j+1])
    ans += solve(i, j+1, h, w-1, nums)
    nums.remove(A[i][j+1])

  return ans


ans = solve(0, 0, H-1,W-1, set([A[0][0]]))
print(ans)