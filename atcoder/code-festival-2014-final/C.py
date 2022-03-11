A = int(input())

def f(n):
  weight = n
  d = 1
  total = 0
  while n > 0:
    total += weight * (n % 10)
    n //= 10
    d *= weight

  return total

for i in range(49,50):
  print(f(i))
    
