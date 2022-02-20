A, B, C, D = (int(x) for x in input().split())

def is_prime(n):
  if n == 1:
    return False

  if n == 2:
    return True

  if n % 2 == 0:
    return False

  i = 3
  while i * i  <= n:
    if n % i == 0:
      return False

    i += 2

  return True
  
ok = False
for i in range(A, B+1):
   if all(not is_prime(i + j) for j in range(C, D+1)):
      ok = True
      break

if ok:
  print("Takahashi")
else:
  print("Aoki")
    