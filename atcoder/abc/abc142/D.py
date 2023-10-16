A, B = (int(x) for x in input().split())

def get_devisors(n):
  i = 1
  ans = set()
  while i**2 <= n:
    if n % i == 0:
      ans.add(i)
      ans.add(n//i)

    i += 1 

  return ans

def is_prime(n):
  if n == 1:
    return False

  if n == 2:
    return True

  if n % 2 == 0:
    return False

  i = 3
  while i**2 <= n:
    if n % i == 0:
      return False

    i += 2

  return True

d1 = get_devisors(A)
d2 = get_devisors(B)
devisors = d1.intersection(d2)
ans = sum(1 for d in devisors if d == 1 or is_prime(d))
print(ans)