from bisect import bisect_left, bisect_right

def find_range_indices(arr, x, y):
  start_index = bisect_left(arr, x)
  end_index = bisect_right(arr, y)

  return start_index, end_index

N, M, D = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
B.sort()

ans = -1
for a in A:
  mn = max(1, a - D)
  mx = a + D
  start, end = find_range_indices(B, mn, mx)
  if start < end:
    ans = max(ans, a + B[end-1])

print(ans)