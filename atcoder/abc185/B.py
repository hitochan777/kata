def solve():
  N, M, T = (int(x) for x in input().split())
  cur = N
  prev = 0
  for _ in range(M):
    A, B = (int(x) for x in input().split())
    cur -= A - prev
    if cur <= 0:
      return False

    cur = min(cur + B - A, N)
    prev = B 
  
  cur -= T - prev
  return cur > 0

print("Yes" if solve() else "No")