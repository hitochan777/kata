from collections import defaultdict, Counter
K = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

fac = factorization(K)
ans = 0
# print(fac)
for k, v in fac:
  cnt = 0
  for i in range(v):
    n = (i+1) * k
    while n % k == 0:
      n //= k
      cnt += 1

    if cnt >= v:
      ans = max(ans, (i+1)*k)
      break

print(ans)