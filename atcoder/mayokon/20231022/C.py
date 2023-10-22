A, B, N = (int(x) for x in input().split())

def f(x):
  return (A * x) // B - A * (x // B)

ans = f(N)
if B-1 <= N:
  ans = max(ans, f(B-1))

print(ans)