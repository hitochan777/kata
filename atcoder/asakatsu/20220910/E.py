from collections import defaultdict

N = int(input())
A = list(int(x) for x in input().split())
count = defaultdict(int)
j = 0
ans = 0
for i in range(N):
  while j < N and count[A[j]] == 0:
    count[A[j]] += 1
    j += 1

  count[A[i]] -= 1
  ans = max(ans, j - i)

print(ans)

    
  
