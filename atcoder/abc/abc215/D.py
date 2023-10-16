N, M = (int(x) for x in input().split())
A = set(int(x) for x in input().split())

factors = set()
def factorization(n):
    added = False
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            factors.add(i)
            added = True

    if temp!=1:
        factors.add(temp)
        added = True

    if not added:
        factors.add(n)

for a in A:
  factorization(a)

ok = [True] * (M + 1)
ptr = 2

while ptr <= M:
  ng = ptr in factors 
  if ng:
    cur = ptr
    while cur <= M:
      ok[cur] = False
      cur += ptr
  else:
    ptr += 1

  while ptr <= M and not ok[ptr]:
    ptr += 1

ans = []
for i in range(1, M+1):
  if ok[i]:
    ans.append(i)

print(len(ans))
for val in ans:
  print(val)

