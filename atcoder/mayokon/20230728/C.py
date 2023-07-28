from collections import Counter
N = int(input())
A = list(int(x) for x in input().split())
A.sort(reverse=True)

acc = [0]
for a in A:
  acc.append(acc[-1]+a)

ans = 0

for i in range(1, N):
  ans += (N-i) * A[i-1]

for i in range(1, N):
  ans -= acc[-1] - acc[i]

print(ans)

   

