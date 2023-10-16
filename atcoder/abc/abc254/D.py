from collections import defaultdict

N = int(input())

square_nums = set()
for i in range(1,N+1):
  square_nums.add(i**2)

divisors = defaultdict(list)
for i in range(1, N+1):
  for j in range(i,N+1,i):
    divisors[j].append(i)

cnt = defaultdict(int)
for i in range(1, N+1):
  for j in range(len(divisors[i])-1, -1, -1):
    if divisors[i][j] in square_nums:
      cnt[i/divisors[i][j]] += 1
      break

ans = 0
for i in range(1, N+1):
  ans += cnt[i]**2

print(ans)