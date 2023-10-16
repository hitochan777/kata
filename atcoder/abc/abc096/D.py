def isPrime(n):
     
    # Corner case
    if n <= 1 or n % 2 == 0:
        return False
 
    i = 3
    while i*i <= n:
      if n % i == 0:
        return False
    
      i += 2
 
    return True
 
# Function to print primes
def getPrimes(n):
  ans = []
  for i in range(2, n + 1):
    if isPrime(i):
      ans.append(i) 

  return ans 

N = int(input())
primes = getPrimes(55555)
ans = []
for p in primes:
  if p % 10 == 3:
    ans.append(p)

print(*ans[:N])
# print(len(primes)