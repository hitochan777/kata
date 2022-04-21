A, B = (int(x) for x in input().split())
def f(n):
  if n % 2 == 0:
    return ((n // 2) % 2) ^ n

  return ((n+1)//2 % 2)

ans = f(A-1) ^ f(B)
print(ans)