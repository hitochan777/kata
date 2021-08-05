def solve():
  N, M, T = (int(x) for x in input().split())
  prev = 0
  for _ in range(M):
    A, B = (int(x) for x in input().split())
    N -= A - prev
    if N <= 0:
      return False

    N += B - A
    prev = B 
  
  N -= T - prev
  return T > 0

print("Yes" if solve() else "No")