A = int(input())

def f(n):
  weight = n
  d = 1
  total = 0
  while n > 0:
    total += d * (n % 10)
    n //= 10
    d *= weight

  return total

for i in range(10, 10**4 + 1):
  if f(i) == A:
    print(i)
    break
else:
  print(-1)
    
